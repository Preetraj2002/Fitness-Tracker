import streamlit as st
from datetime import datetime, timedelta
from FrontEnd.foodPage import food_calorie_tracker
from FrontEnd.sleepPage import sleep_quality_tracker
from FrontEnd.profilePage import show_profile
from FrontEnd.waterPage import water_intake_tracker
def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Food Calorie Tracker', 'Sleep Quality Tracker', 'Profile', 'Water Intake Tracker'])

    if selection == 'Food Calorie Tracker':
        food_calorie_tracker()
    elif selection == 'Sleep Quality Tracker':
        sleep_quality_tracker()
    elif selection == 'Profile':
        show_profile()
    elif selection == 'Water Intake Tracker':
        water_intake_tracker()

if __name__ == "__main__":
    main()
