import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objects as go
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

    # plt.style.use('dark_background')

    # Create a Plotly figure
    fig = go.Figure()

    # Add a line trace for the water intake data
    fig.add_trace(go.Scatter(x=water_df.date_column, y=water_df['total_water_ml'], mode='lines+markers', name='Water Intake'))

    # Update layout properties
    fig.update_layout(
        title="Daily Water Intake",
        yaxis_title="Total Water Intake (ml)",
        xaxis_tickformat='%d-%b',  # Customize x-axis tick labels to show only date and month
        xaxis_tickangle=-45,  # Rotate x-axis tick labels
        xaxis_showgrid=True,  # Add gridlines
        yaxis_showgrid=True,
    )

    # Display the interactive plot
    st.plotly_chart(fig)

    calories_df = fetch_calories(user_id, cur)

    # Create a Plotly figure
    fig = go.Figure()

    # Add a line trace for the daily calories burnt
    fig.add_trace(go.Scatter(x=calories_df['date_column'], y=calories_df['total_calories_burnt'], mode='lines+markers', name='Calories Burnt'))

    # Update layout properties
    fig.update_layout(
        title="Daily Calories Burnt",
        yaxis_title="Total Calories Burnt",
        xaxis_tickformat='%d-%b',  # Customize x-axis tick labels to show only date and month
        xaxis_tickangle=-45,  # Rotate x-axis tick labels
        xaxis_showgrid=True,  # Add gridlines
        yaxis_showgrid=True,
        # plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
        # paper_bgcolor='rgba(0,0,0,0)',  # Set paper background color to transparent
    )

    # Display the plot
    st.plotly_chart(fig)

    sleep_df = fetch_sleep_time(user_id, cur)

    # Create a Plotly figure
    fig = go.Figure()

    # Add a line trace for the daily sleep duration
    fig.add_trace(go.Scatter(x=sleep_df['date_column'], y=sleep_df['total_sleep'], mode='lines+markers', name='Sleep Duration'))

    # Update layout properties
    fig.update_layout(
        title="Daily Sleep Duration",
        yaxis_title="Total Sleep (hours)",
        xaxis_tickformat='%d-%b',  # Customize x-axis tick labels to show only date and month
        xaxis_tickangle=-45,  # Rotate x-axis tick labels
        xaxis_showgrid=True,  # Add gridlines
        yaxis_showgrid=True,
    )

    # Display the plot
    st.plotly_chart(fig)

    # Calculate total sleep duration for each sleep stage
    light_sleep_total = sleep_df['light_sleep'].sum()
    deep_sleep_total = sleep_df['deep_sleep'].sum()
    rem_sleep_total = sleep_df['rem_sleep'].sum()

    # Create labels and corresponding values for the pie chart
    labels = ['Light Sleep', 'Deep Sleep', 'REM Sleep']
    values = [light_sleep_total, deep_sleep_total, rem_sleep_total]

    # Define colors for each sleep stage
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    from plotly.colors import sequential

    colorscale = sequential.Viridis
    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3 ,marker_colors=colorscale,
                    textinfo='value+percent', textposition='inside',
                    textfont=dict(size=20,color='white'))])


    # Update layout properties
    fig.update_layout(
        title="Sleep Distribution",
    )

    # Display the plot
    st.plotly_chart(fig)


    # food_df = fetch_food_intake(user_id, cur)






    cur.close()