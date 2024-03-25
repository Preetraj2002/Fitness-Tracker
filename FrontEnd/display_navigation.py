import streamlit as st
import cx_Oracle
from datetime import datetime, timedelta
from FrontEnd.foodPage import food_calorie_tracker
from FrontEnd.sleepPage import sleep_quality_tracker
from FrontEnd.profilePage import show_profile
from FrontEnd.waterPage import water_intake_tracker
from FrontEnd.loginPage import user_login
from FrontEnd.motivation import show_motivational_quote
from streamlit_option_menu import option_menu

def connect_to_database1():
    connStr = "system/chand123@localhost:1521/xepdb1"
    conn = cx_Oracle.connect(connStr)
    return conn


from PIL import Image
im=Image.open('Asset/logo.png')

def navigation(user_id, conn):
    # If user is logged in, show the selected page
    if user_id:
        st.empty()
        with st.sidebar:        
            app = option_menu(
                menu_title='Fitness-Tracker',
                options=['Profile','Food','Sleep','Water','Get Motivation','Logout'],
                icons=['person-fill','cake-fill','moon-fill','water','sun-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=4,
                styles={
                    "container": {"padding": "5!important","background-color":'#080808',"color":"#e4e0e0"},# pkc=#eaf8db
        "icon": {"color": "#1f211c", "font-size": "23px"}, 
        "nav-link": {"color":"#e4e0e0","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#1f211c"},
        "nav-link-selected": {"background-color": "yellow","color":"#1f211c"},} # pdc=fg
                
                )

        
        if app == "Food":
          food_calorie_tracker(user_id, conn)
        if app == "Sleep":
            sleep_quality_tracker(user_id, conn)     
        if app == 'Water':
            water_intake_tracker(user_id, conn)
        if app == "Profile":
            show_profile(user_id, conn)  
        if app == "Get Motivation":
            show_motivational_quote()
        if app == 'Logout':
            session_state = st.session_state
            session_state.user_id = None
            st.success("Logout successful")
            user_login()
