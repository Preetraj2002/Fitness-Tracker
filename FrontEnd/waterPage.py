import streamlit as st
from datetime import datetime, timedelta

# def water_intake_tracker(user_id, conn):
#     st.title("Water Intake Tracker")

#     # Date selection
#     selected_date = st.date_input("Select Date")

#     # Time selection
#     selected_time = st.time_input("Select Time")

#     # Quantity input
#     quantity = st.number_input("Enter Quantity (in ml)", min_value=0)

#     # Submit button
#     if st.button("Submit"):
#         st.success(f"Logged Water Intake: {quantity} ml at {selected_date} on {selected_time}")


def insert_water_intake(conn, user_id, time_stamp, quantity_ml):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO water_intake (user_id, time_stamp, quantity_ml) VALUES (:user_id, :time_stamp, :quantity_ml)",
        {"user_id": user_id, "time_stamp": time_stamp, "quantity_ml": quantity_ml},
    )
    conn.commit()
    cur.close()


def water_intake_tracker(user_id, conn):
    st.title("Water Intake Tracker")

    # Date selection
    selected_date = st.date_input("Select Date")

    # Time selection
    selected_time = st.time_input("Select Time")

    # Combine date and time into a single datetime object
    time_stamp = datetime.combine(selected_date, selected_time)

    # Quantity input
    quantity = st.number_input("Enter Quantity (in ml)", min_value=0)

    # Submit button
    if st.button("Submit", type="primary"):
        insert_water_intake(conn, user_id, time_stamp, quantity)
        st.success(
            f"Logged Water Intake: {quantity} ml at {selected_date} on {selected_time}"
        )
