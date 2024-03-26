import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
from PIL import Image

def user_info(user_id, cur):
    cur.execute(
        'SELECT * FROM "user" WHERE id = :user_id',
        {"user_id": user_id},
    )
    row = cur.fetchone()
    if row is not None:
        sex = row[2]
        age = row[3]
        wt = row[4]
        ht = row[5]
    
    return sex, age, wt, ht


def fetch_calories(user_id, cur):
   # Define SQL query to retrieve exercise data for the specified user
    exercise_query = f"""
    SELECT TRUNC(time_stamp) AS date_column, sum(calories_burnt) AS total_calories_burnt
    FROM exercise_log
    WHERE user_id = {user_id}
    GROUP BY TRUNC(time_stamp)
    """
    cur.execute(exercise_query)
    rows = cur.fetchall()

    # Convert exercise data to DataFrame
    df = pd.DataFrame(rows, columns=['date_column', 'total_calories_burnt'])
    st.write(df)
    return df


def fetch_water_intake(user_id, cur):
    # Define SQL query to retrieve water intake data for the specified user
    water_query = f"""
    SELECT TRUNC(time_stamp) AS date_column, sum(quantity_ml) AS total_water_ml
    FROM water_intake
    WHERE user_id = {user_id}
    GROUP BY TRUNC(time_stamp)
    """
    cur.execute(water_query)
    rows = cur.fetchall()   # list of tuples
    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=['date_column', 'total_water_ml'])
    st.write(df)
    return df

def fetch_sleep_time(user_id, cur):
    # Define SQL query to retrieve sleep data for the specified user
    sleep_query = f"""
    SELECT TRUNC(time_stamp) AS date_column, sum(totalduration) AS total_sleep,sum(light) AS light_sleep,sum(deep) AS deep_sleep, sum(rem) AS rem_sleep
    FROM sleep
    WHERE userid = {user_id}
    GROUP BY TRUNC(time_stamp)
    """ 
    cur.execute(sleep_query)
    rows = cur.fetchall()   # list of tuples
    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=['date_column', 'total_sleep', 'light_sleep', 'deep_sleep', 'rem_sleep'])
    st.write(df)
    return df


def fetch_food_intake(user_id, cur):
    # Define SQL query to retrieve food intake data for the specified user
    food_query = f"""
    SELECT TRUNC(time_stamp) AS date_column, sum(calories) AS total_calories
    FROM foodlog
    WHERE userid = {user_id}
    GROUP BY TRUNC(time_stamp),  
    """

    cur.execute(food_query)
    rows = cur.fetchall()   # list of tuples

    # Convert to DataFrame
    food_df = pd.DataFrame(rows, columns=['date_column', 'total_calories'])

    # Display the DataFrame
    st.write(food_df)

    # Return the DataFrame
    return food_df



def show_charts(user_id, conn):

    cur = conn.cursor()

    # Fetch data from Oracle database
    age ,sex, weight_kg, height_cm = user_info(user_id, cur)

    data = {
        "Attribute": ["Age",  "Sex", "Calories Weight(kg)", "Height(cm)"],
        "Value": [age, sex, weight_kg, height_cm],
    }
    df = pd.DataFrame(data)

    user_df = df.style.hide(axis='index')
    user_df.hide(axis='columns')
    
    st.write(user_df.to_html(), unsafe_allow_html=True)

    water_df = fetch_water_intake(user_id, cur)

    # Display Water Intake
    st.write(f"## Daily Water Intake for User {user_id}")
    st.line_chart(water_df.set_index('date_column'))
    # Set up the plot
    # plt.rcParams.update({'axes.facecolor':'black'})
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 6))
    plt.plot(water_df.date_column, water_df['total_water_ml'], marker='.', linestyle='-', color='b')
    plt.title("Daily Water Intake")
    plt.xlabel('Date')
    plt.ylabel('Total Water Intake (ml)')
    plt.xticks(rotation=45)
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
    # Customize x-axis tick labels to show only date and month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
    # Display the plot
    st.pyplot(fig)

    calories_df = fetch_calories(user_id, cur)

    # Display Calories Burnt
    st.write(f"## Daily Calories Burnt for User {user_id}")
    st.line_chart(calories_df.set_index('date_column'))

    fig = plt.figure(figsize=(10, 6))

    # Plot the daily calories burnt
    plt.plot(calories_df.date_column, calories_df['total_calories_burnt'], marker='.', linestyle='-', color='r')

    # Set plot title and axis labels
    plt.title("Daily Calories Burnt")
    plt.xlabel('Date')
    plt.ylabel('Total Calories Burnt')

    # Rotate x-axis tick labels
    plt.xticks(rotation=45)

    # Add gridlines
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

    # Customize x-axis tick labels to show only date and month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))

    # Display the plot
    st.pyplot(fig)

    sleep_df = fetch_sleep_time(user_id, cur)
    fig = plt.figure(figsize=(10, 6))

    # Plot the Sleep Duration
    plt.plot(sleep_df.date_column, sleep_df['total_sleep'], marker='.', linestyle='-', color='r')

    # Set plot title and axis labels
    plt.title("Daily Sleep Duration")
    plt.xlabel('Date')
    plt.ylabel('Total Sleep(hours)')

    # Rotate x-axis tick labels
    plt.xticks(rotation=45)

    # Add gridlines
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

    # Customize x-axis tick labels to show only date and month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))

    # Display the plot
    st.pyplot(fig)

    # Create pie chart

    light_sleep = sleep_df['light_sleep'].sum()
    deep_sleep = sleep_df['deep_sleep'].sum()
    rem_sleep = sleep_df['rem_sleep'].sum()

    # Create labels and corresponding values for the pie chart
    labels = ['Light Sleep', 'Deep Sleep', 'REM Sleep']
    sizes = [light_sleep, deep_sleep, rem_sleep]
    # Define colors for each partition
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Set plot title
    st.markdown("## Sleep Distribution")

    # Display the plot
    st.pyplot(fig)


    # food_df = fetch_food_intake(user_id, cur)






    cur.close()