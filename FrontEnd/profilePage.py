import streamlit as st
# Sample user data (replace with actual user data)
user_data = {
    "username": "JohnDoe",
    "bmi": 25.5  # Example BMI value
}

def show_profile():
    st.title("Profile")
    st.write(f"Username: {user_data['username']}")
    st.write(f"BMI: {user_data['bmi']}")
