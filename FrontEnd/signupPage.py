import streamlit as st
import cx_Oracle
from datetime import datetime
from FrontEnd.loginPage import authenticate_user


def connect_to_database():
    connStr = "system/prakriti1@localhost:1521/xepdb1"
    conn = cx_Oracle.connect(connStr)
    return conn


def user_signup():
    conn = connect_to_database()
    cur = conn.cursor()
    st.title("Sign Up")
    name = st.text_input("Name")
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=0, max_value=150)
    weight_kg = st.number_input("Weight (kg)", min_value=0.0)
    height_cm = st.number_input("Height (cm)", min_value=0.0)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    userid = None
    if st.button("Sign Up"):
        cur.execute(
            'INSERT INTO "user" (name, sex, age, weight_kg, height_cm, username, password) VALUES (:name, :sex, :age, :weight_kg, :height_cm, :username, :password)',
            {
                "name": name,
                "sex": sex,
                "age": age,
                "weight_kg": weight_kg,
                "height_cm": height_cm,
                "username": username,
                "password": password,
            },
        )
        conn.commit()
        st.success("Sign up successful.")
        userid = authenticate_user(username, password)
    cur.close()
    conn.close()
    return userid
