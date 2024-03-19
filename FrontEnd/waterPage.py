import streamlit as st
def water_intake_tracker():
    st.title("Water Intake Tracker")

    # Date selection
    selected_date = st.date_input("Select Date")

    # Time selection
    selected_time = st.time_input("Select Time")

    # Quantity input
    quantity = st.number_input("Enter Quantity (in ml)", min_value=0)

    # Submit button
    if st.button("Submit"):
        st.success(f"Logged Water Intake: {quantity} ml at {selected_date} on {selected_time}")
