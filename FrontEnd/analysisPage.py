import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objects as go
from plotly.colors import sequential
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

# Define function to plot data based on granularity
def plot_data(df, title, x_axis_title, y_axis_title, granularity):
    fig = go.Figure()

    # Check if the DataFrame is empty
    if not df.empty:
        if granularity == 'Daily':
            # Plot line chart for daily data
            fig.add_trace(go.Scatter(x=df['date_column'], y=df['total_data'], mode='lines+markers'))
        elif granularity == 'Weekly':
            # Plot bar chart for weekly data
            text_inside_bars = df['week_number'] + '<br>' + df['total_data'].astype(str)
            fig.add_trace(go.Bar(x=df['week_number'], y=df['total_data'], text=text_inside_bars,
                            textposition='inside', 
                            hoverinfo='x+text'))
        elif granularity == 'Monthly':
            # Plot bar chart for monthly data
            month_names = []

            for month_year in df['month']:
                # Split the string to extract month and year
                year, month = month_year.split('-')
                
                # Get the month name from the month number
                month_name = datetime.date(int(year), int(month), 1).strftime("%B")
                month_names.append(month_name)

            # Concatenate month name and total data values for displaying inside the bars
            text_inside_bars = [f"{month}<br>{total}" for month, total in zip(month_names, df['total_data'])]

            fig.add_trace(go.Bar(
                x=month_names,
                y=df['total_data'],
                text=text_inside_bars,  # Display month name and total data inside the bars
                textposition='inside',  # Position the text inside the bars
                hoverinfo='text'  # Display only text on hover
            ))
            
    # Update layout properties
    fig.update_layout(
        title=title,
        # xaxis_title=x_axis_title,
        yaxis_title=y_axis_title,
        # xaxis_tickformat='%d-%b',  # Customize x-axis tick labels to show only date and month
        xaxis_tickangle=-45,  # Rotate x-axis tick labels
        xaxis_showgrid=True,  # Add gridlines
        yaxis_showgrid=True,
    )

    # Display the Plotly figure using Streamlit
    st.plotly_chart(fig)


def fetch_calories(user_id, cur,granularity):
   # Define SQL query to retrieve exercise data for the specified user
    
    if granularity == "Daily":
        exercise_query = f"""
        SELECT TRUNC(time_stamp) AS date_column, sum(calories_burnt) AS total_data
        FROM exercise_log
        WHERE user_id = {user_id}
        GROUP BY TRUNC(time_stamp)
        """

    elif granularity == "Weekly":
        exercise_query = f"""
        SELECT TO_CHAR(time_stamp, 'IYYY-IW') AS week_number,SUM(calories_burnt) AS total_data
        FROM exercise_log
        WHERE user_id = {user_id}
        GROUP BY TO_CHAR(time_stamp, 'IYYY-IW')
        ORDER BY week_number
        """

    else :
        exercise_query = f"""
        SELECT TO_CHAR(time_stamp, 'YYYY-MM') AS month ,SUM(calories_burnt) AS total_data
        FROM exercise_log
        WHERE user_id = {user_id}
        GROUP BY TO_CHAR(time_stamp, 'YYYY-MM')
        ORDER BY month
        """


    cur.execute(exercise_query)
    rows = cur.fetchall()

    if granularity == "Daily":
        df = pd.DataFrame(rows, columns=['date_column', 'total_data'])
    elif granularity == "Weekly":
        df = pd.DataFrame(rows, columns=['week_number', 'total_data'])
    else :
        df = pd.DataFrame(rows, columns=['month', 'total_data'])

    # Display the DataFrame
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

    st.divider()
    # Add a slider to select the granularity (weekly or daily)
    granularity = st.select_slider('Select Granularity', options =['Daily','Weekly','Monthly'],value='Daily')

    # Based on the selected granularity, display the appropriate chart
    if granularity == 'Weekly':
        st.write("Weekly Chart")
        # Plot the weekly chart here using the Plotly or Matplotlib code for weekly data
    elif granularity == 'Monthly':
        st.write("Monthly Chart")
    else:
        st.write("Daily Chart")
        # Plot the daily chart here using the Pl



    water_df = fetch_water_intake(user_id, cur)

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

    st.divider()

    calories_df = fetch_calories(user_id, cur,granularity)
    plot_data(calories_df, "Calories Burnt", "Date", "Calories", granularity)

   
    st.divider()

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