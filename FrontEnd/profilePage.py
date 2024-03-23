import streamlit as st
# Sample user data (replace with actual user data)
# user_data = {
#     "username": "JohnDoe",
#     "bmi": 25.5  # Example BMI value
# }

def show_profile(user_id, conn):
    cur = conn.cursor()
    cur.execute('SELECT name, sex, age, weight_kg, height_cm, bmi FROM "user" WHERE id = :user_id', {'user_id': user_id})
    user_data = cur.fetchone()
    st.title("Profile")
    st.write(f"Name: {user_data[0]}")
    st.write(f"Sex: {user_data[1]}")
    st.write(f"Age: {user_data[2]}")
    st.write(f"Weight (kg): {user_data[3]}")
    st.write(f"Height (cm): {user_data[4]}")
    st.write(f"BMI: {user_data[5]}")
