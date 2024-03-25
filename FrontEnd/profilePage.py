import streamlit as st
from PIL import Image
# Sample user data (replace with actual user data)
# user_data = {
#     "username": "JohnDoe",
#     "bmi": 25.5  # Example BMI value
# }

# def show_profile(user_id, conn):
#     cur = conn.cursor()
#     cur.execute('SELECT name, sex, age, weight_kg, height_cm, bmi FROM "user" WHERE id = :user_id', {'user_id': user_id})
#     user_data = cur.fetchone()
#     st.title("Profile")
#     st.write(f"Name: {user_data[0]}")
#     st.write(f"Sex: {user_data[1]}")
#     st.write(f"Age: {user_data[2]}")
#     st.write(f"Weight (kg): {user_data[3]}")
#     st.write(f"Height (cm): {user_data[4]}")
#     st.write(f"BMI: {user_data[5]}")


def edit_profile(user_id, conn):
    cur = conn.cursor()
    cur.execute(
        'SELECT name, sex, age, weight_kg, height_cm, bmi FROM "user" WHERE id = :user_id',
        {"user_id": user_id},
    )
    user_data = cur.fetchone()

    new_name = st.text_input("Name", user_data[0])
    new_sex = st.radio(
        "Sex", ["Male", "Female"], index=0 if user_data[1] == "Male" else 1
    )
    new_age = st.number_input("Age", value=user_data[2])
    new_weight = st.number_input("Weight (kg)", value=user_data[3])
    new_height = st.number_input("Height (cm)", value=user_data[4])

    if st.button("Update Profile"):
        cur.execute(
            'UPDATE "user" SET name = :name, sex = :sex, age = :age, weight_kg = :weight, height_cm = :height WHERE id = :user_id',
            {
                "name": new_name,
                "sex": new_sex,
                "age": new_age,
                "weight": new_weight,
                "height": new_height,
                "user_id": user_id,
            },
        )
        conn.commit()
        st.success("Profile updated successfully!")


def show_profile(user_id, conn):
    
    im=Image.open('Asset/runner.png') 
    # Streamlit app layout
   # Assuming 'im' is your image variable
    col1, col2 = st.columns([1, 5])
    with col1:
        # Display the grayscale image
        st.image(im, width=100)

    with col2:
        st.title("Profile")
    cur = conn.cursor()
    cur.execute(
        'SELECT name, sex, age, weight_kg, height_cm, bmi FROM "user" WHERE id = :user_id',
        {"user_id": user_id},
    )
    user_data = cur.fetchone()

    edit_mode = st.button("Edit Profile")

    if edit_mode:
        edit_profile(user_id, conn)
    else:
        info_style = "font-size: 18px; padding: 10px; background-color: black; border-radius: 5px;"

        st.write(f"<p style='{info_style}'><b>Name:</b> {user_data[0]}</p>", unsafe_allow_html=True)
        st.write(f"<p style='{info_style}'><b>Sex:</b> {user_data[1]}</p>", unsafe_allow_html=True)
        st.write(f"<p style='{info_style}'><b>Age:</b> {user_data[2]}</p>", unsafe_allow_html=True)
        st.write(f"<p style='{info_style}'><b>Weight (kg):</b> {user_data[3]}</p>", unsafe_allow_html=True)
        st.write(f"<p style='{info_style}'><b>Height (cm):</b> {user_data[4]}</p>", unsafe_allow_html=True)
        st.write(f"<p style='{info_style}'><b>BMI:</b> {user_data[5]}</p>", unsafe_allow_html=True)

