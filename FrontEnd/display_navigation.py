import streamlit as st
import cx_Oracle
from datetime import datetime, timedelta
from FrontEnd.foodPage import food_calorie_tracker
from FrontEnd.sleepPage import sleep_quality_tracker
from FrontEnd.profilePage import show_profile
from FrontEnd.waterPage import water_intake_tracker
from FrontEnd.loginPage import user_login


def connect_to_database1():
    connStr = "system/prakriti1@localhost:1521/xepdb1"
    conn = cx_Oracle.connect(connStr)
    return conn


def navigation(user_id, conn):
    # If user is logged in, show the selected page
    if user_id:
        st.empty()
        selection = st.sidebar.radio(
            "Go to",
            [
                "Food Calorie Tracker",
                "Sleep Quality Tracker",
                "Profile",
                "Water Intake Tracker",
                "Logout",
            ],
        )
        if selection == "Food Calorie Tracker":
            food_calorie_tracker(user_id, conn)
        elif selection == "Sleep Quality Tracker":
            sleep_quality_tracker(user_id, conn)
        elif selection == "Profile":
            show_profile(user_id, conn)
        elif selection == "Water Intake Tracker":
            water_intake_tracker(user_id, conn)
        elif selection == "Logout":
            session_state = st.session_state
            session_state.user_id = None
            st.success("Logout successful")
            user_login()
