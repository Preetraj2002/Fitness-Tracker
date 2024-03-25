import streamlit as st
import cx_Oracle
from datetime import datetime, timedelta
from FrontEnd.loginPage import user_login
from FrontEnd.display_navigation import navigation
from FrontEnd.signupPage import user_signup
from PIL import Image

def connect_to_database():
    connStr = "system/prakriti1@localhost:1521/xepdb1"
    conn = cx_Oracle.connect(connStr)
    return conn

im=Image.open('Asset/logo.png')

def main():
    conn = connect_to_database()
    cur = conn.cursor()
    st.sidebar.title("Fitness-Tracker").image(im,width=300)
    selection = st.sidebar.radio(
        "Go to",
        [
            "Sign Up",
            "Login",
        ],
    )

    # Check if the user is already logged in
    session_state = st.session_state
    if "user_id" not in session_state:
        session_state.user_id = None

    # If user is not logged in, show the login page
    if session_state.user_id is None:
        # session_state.user_id = user_login()
        # if st.button("Login"):
        #     session_state.user_id = user_login()
        # if st.button("Sign Up"):
        #     session_state.user_id = user_signup()
        if selection == "Sign Up":
            session_state.user_id = user_signup()
        elif selection == "Login":
            session_state.user_id = user_login()

    navigation(session_state.user_id, conn)


if __name__ == "__main__":
     st.set_page_config(page_title="Fitness-Tracker-App", page_icon=im)
    main()
