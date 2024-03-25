import streamlit as st
from datetime import datetime
from PIL import Image
# def calculate_sleep_index(
#     total_duration, deep_sleep_duration, light_sleep_duration, rem_sleep_duration
# ):
#     # Calculate Sleep Efficiency
#     sleep_efficiency = (
#         (deep_sleep_duration + light_sleep_duration + rem_sleep_duration)
#         / total_duration
#     ) * 100

#     # Calculate Sleep Index
#     if sleep_efficiency < 85:
#         sleep_index = "Poor"
#     elif 85 <= sleep_efficiency < 90:
#         sleep_index = "Fair"
#     elif 90 <= sleep_efficiency < 95:
#         sleep_index = "Good"
#     else:
#         sleep_index = "Excellent"

#     return sleep_index


# def sleep_quality_tracker( user_id, conn):
#     st.title("Sleep Quality Tracker")

#     # Timestamp input
#     timestamp = st.date_input("Date")

#     # Total duration input
#     total_duration = st.number_input("Total Sleep Duration (minutes)")

#     # Deep sleep duration input
#     deep_sleep_duration = st.number_input("Deep Sleep Duration (minutes)")

#     # Light sleep duration input
#     light_sleep_duration = st.number_input("Light Sleep Duration (minutes)")

#     # REM sleep duration input
#     rem_sleep_duration = st.number_input("REM Sleep Duration (minutes)")

#     # Submit button
#     if st.button("Submit"):
#         # Calculate sleep index
#         sleep_index = calculate_sleep_index(
#             total_duration,
#             deep_sleep_duration,
#             light_sleep_duration,
#             rem_sleep_duration,
#         )

#         # Display sleep index
#         st.success(f"Sleep Index: {sleep_index}")


def insert_sleep_data(
    conn,
    user_id,
    time_stamp,
    total_duration,
    deep_duration,
    light_duration,
    rem_duration,
    sleep_quality_index,
):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Sleep (UserID, time_stamp, TotalDuration, Deep, Light, Rem, SleepQualityIndex) VALUES (:user_id, :time_stamp, :total_duration, :deep_duration, :light_duration, :rem_duration, :sleep_quality_index)",
        {
            "user_id": user_id,
            "time_stamp": time_stamp,
            "total_duration": total_duration,
            "deep_duration": deep_duration,
            "light_duration": light_duration,
            "rem_duration": rem_duration,
            "sleep_quality_index": sleep_quality_index,
        },
    )
    conn.commit()
    cur.close()


def calculate_sleep_quality_index(
    total_duration, deep_duration, light_duration, rem_duration
):
    # Calculate Sleep Quality Index
    sleep_quality_index = (
        ((deep_duration / total_duration) * 0.25)
        + ((light_duration / total_duration) * 0.5)
        + ((rem_duration / total_duration) * 0.25)
    )
    return sleep_quality_index


def sleep_quality_tracker(user_id, conn):
    im=Image.open('Asset/sleep.png') 
    # Streamlit app layout
   # Assuming 'im' is your image variable
    col1, col2 = st.columns([1, 5])
    with col1:
        # Display the grayscale image
        st.image(im, width=100)

    with col2:
        st.title("Sleep Quality Tracker")

    # Date selection
    selected_date = st.date_input("Select Date")

    # Time selection
    selected_time = st.time_input("Select Time")

    # Combine date and time into a single datetime object
    time_stamp = datetime.combine(selected_date, selected_time)

    # Total duration input
    total_duration = st.number_input("Total Sleep Duration (hours)")

    # Deep sleep duration input
    deep_duration = st.number_input("Deep Sleep Duration (hours)")

    # Light sleep duration input
    light_duration = st.number_input("Light Sleep Duration (hours)")

    # REM sleep duration input
    rem_duration = st.number_input("REM Sleep Duration (hours)")

    # Calculate sleep quality index
    if total_duration:
        sleep_quality_index = calculate_sleep_quality_index(
            total_duration, deep_duration, light_duration, rem_duration
        )

    # Submit button
    if st.button("Submit", type="primary"):
        insert_sleep_data(
            conn,
            user_id,
            time_stamp,
            total_duration,
            deep_duration,
            light_duration,
            rem_duration,
            sleep_quality_index,
        )
        st.success("Sleep data logged successfully.")
