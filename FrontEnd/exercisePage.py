import streamlit as st
import datetime
import pandas as pd

exercise_list = [
    "Yoga",
    "Walking",
    "Running",
    "Cricket",
    "Badminton",
    "Swimming",
    "Cycling",
    "Aerobics/Zumba",
    "Traditional Dance",
    "Skipping",
    "Martial Arts",
    "Misc"
]

def calories_burnt(conn, user_id, exercise, duration):
    cur = conn.cursor()
    cur.execute(
        'SELECT weight_kg FROM "user" WHERE id = :user_id',
        {"user_id": user_id},
    )
    usr_row = cur.fetchone()
  
    if cur.rowcount > 0:
        wt = usr_row[0]
    cur.execute(
        'SELECT met_value,description FROM met_value_table WHERE exercise = :exercise',
        {"exercise": exercise},
    )

    exer_row = cur.fetchone()
    if cur.rowcount > 0:
        MET = exer_row[0]
        desc = exer_row[1]
    cur.close()
    return round((wt*MET*duration)/60,2),MET

def add_exercise(conn, user_id, time_stamp,exercise,duration,cals):
    cur = conn.cursor()
    cur.execute(
       """ INSERT INTO exercise_log (time_stamp, user_id, exercise_type, duration_hours, calories_burnt)
            VALUES (:time_stamp, :user_id, :exercise_type, :duration_hours, :calories_burnt) """,
       
       {"time_stamp": time_stamp, "user_id": user_id, "exercise_type": exercise, 
        "duration_hours": duration, "calories_burnt": cals},
    )
    conn.commit()
    cur.close()

def exercise_tracker(user_id, conn):
# Streamlit app layout
    st.title("Exercise Tracker 🏃")

    # Date input
    date = st.date_input("Select Date")

    # Time slot selection
    time = st.time_input('Select Time Slot', datetime.time(8, 45))

    # Combine date and time into a datetime object
    timestamp = datetime.datetime.combine(date, time)

    # Exercise selection
    exercise = st.selectbox("Select Exercise", exercise_list)

    # Duration input
    duration = st.number_input("Enter Duration (in minutes)", min_value=5)


    # Submit button
    if st.button("Submit"):
        # Calculate calories
        calories,MET = calories_burnt(conn,user_id,exercise, duration)
        
        # Display result

        data = {
            "Attribute": ["Exercise",  "MET Value", "Calories Burnt"],
            "Value": [exercise,  MET, calories]
        }
        df = pd.DataFrame(data)

        styled_df = df.style.hide(axis='index').format(precision=2)
        styled_df.hide(axis='columns')
        
        st.write(styled_df.to_html(), unsafe_allow_html=True)
        st.markdown("") 
        add_exercise(conn, user_id, timestamp, exercise, duration, calories)
        st.success("Exercise Logged!")
