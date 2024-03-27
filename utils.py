# Import necessary libraries
import smtplib
from datetime import datetime, timedelta
import cx_Oracle
import time
import os
from dotenv import load_dotenv
# Load the environment variables from the `.env` file
load_dotenv()




def fetch_fitness_data(user_id):

    # Connect to the database
    conn = cx_Oracle.connect("system/12345678@localhost:1521/xepdb1")
    cur = conn.cursor()

    # Retrieve fitness data for today
    today = datetime.now().date()

    # Query to retrieve calories consumed today
    calories_in_query = """
    SELECT SUM(calories_consumed) AS total_calories_consumed
    FROM foodlog
    WHERE user_id = :user_id AND TRUNC(time_stamp) = :today
    """

    # Query to retrieve calories burnt today
    calories_burnt_query = """
    SELECT SUM(calories_burnt) AS total_calories_burnt
    FROM exercise_log
    WHERE user_id = :user_id AND TRUNC(time_stamp) = :today
    """

    # Query to retrieve water intake today
    water_intake_query = """
    SELECT SUM(quantity_ml) AS total_water_intake
    FROM water_intake
    WHERE  user_id = :user_id AND TRUNC(time_stamp) = :today
    """

    # Fetch calories consumed today
    # cur.execute(calories_in_query,user_id=user_id, today=today)
    # calories_in_today = cur.fetchone()[0] or 0
    calories_in_today = 2000

    # Fetch calories burnt today
    cur.execute(calories_burnt_query,user_id=user_id, today=today)
    calories_burnt_today = cur.fetchone()[0] or 0

    # Fetch water intake today
    cur.execute(water_intake_query,user_id=user_id, today=today)
    water_intake_today = cur.fetchone()[0] or 0

    # Retrieve fitness data for the previous day
    yesterday = today - timedelta(days=1)

    # Query to retrieve sleep duration for yesterday
    sleep_duration_query = """
    SELECT SUM(totalduration) AS total_sleep_duration
    FROM sleep
    WHERE userid = :user_id AND TRUNC(time_stamp) = :yesterday
    """

    # Fetch sleep duration for yesterday
    cur.execute(sleep_duration_query,user_id=user_id, yesterday=yesterday)
    sleep_duration_yesterday = cur.fetchone()[0] or 0

    cur.execute(
        'SELECT * FROM "user" WHERE id = :user_id',
        {"user_id": user_id},
    )
    row = cur.fetchone()
    if row is not None:
        name = row[1]
        sex = row[2]
        age = row[3]
        wt = row[4]
        ht = row[5]

    cur.close()
    conn.close()

    data = {
        'name': name,
        'sex': sex,
        'age': age,
        'wt': wt,
        'ht': ht,
        'calories_in_today': calories_in_today,
        'calories_burnt_today': calories_burnt_today,
        'water_intake_today': water_intake_today,
        'sleep_duration_yesterday': sleep_duration_yesterday,
    }

    return data


# Function to send email
def send_email(user_id,user_mail="preetrajgupta2002@gmail.com"):
   # Set up SMTP connection
    sender = "preetrajgupta2002@gmail.com"
    receiver = user_mail
    password =os.environ.get('SMTP_PASSWORD')

    # Retrieve fitness data for today
    today = datetime.now().date()
    data = fetch_fitness_data(user_id)
    name = data['name']
    calories_in_today = data['calories_in_today']  
    calories_burnt_today = data['calories_burnt_today'] 
    water_intake_today = data['water_intake_today']

    # Retrieve fitness data for the previous day
    yesterday = today - timedelta(days=1)
    sleep_duration_yesterday = data['sleep_duration_yesterday']

    # Format email message
    subject = f"Daily Fitness Report - {today}"
    body = f"Hey! {name},\n\nDaily Fitness Report for {today}:\n\n"
    body += f"Calories In: {calories_in_today}\n"
    body += f"Calories Burnt: {calories_burnt_today}\n"
    body += f"Water Intake: {water_intake_today}\n"
    body += f"\n\nYour sleep duration yesterday (on {yesterday}) was {sleep_duration_yesterday} hours."

    # Check for recommendations based on data
    recommendations = []
    if calories_in_today > calories_burnt_today:
        recommendations.append("Consider reducing your calorie intake to maintain a balance.")
    elif calories_in_today < calories_burnt_today:
        recommendations.append("Ensure you're consuming enough calories to meet your energy needs.")
    if water_intake_today < 2000:
        recommendations.append("Drink more water to stay hydrated throughout the day.")

    # Add recommendations to email body
    if recommendations:
        body += "\n\nRecommendations:\n"
        body += "\n".join(recommendations)

    # Compose email
    message = f"Subject: {subject}\n\n{body}"

    
    # Check if the current time is after 11 PM
    now = datetime.now()
    if now.hour >= 23:
        try:
            # Connect to the SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                # Send the email
                server.sendmail(sender, receiver, message)
                print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")
    else:
        print("It's not yet 11 PM. No email will be sent.")

# Schedule the script to run every day
while True:
    # Check the current time
    now = datetime.now()
    print(now)
    # If it's after 11 PM, send the email
    if now.hour >= 23:
        # Send email for each user
        conn = cx_Oracle.connect("system/12345678@localhost:1521/xepdb1")
        cur = conn.cursor()
        # cur.execute("""SELECT id FROM "user" """)
        # user_ids =[id[0] for id in cur.fetchall()]
        cur.execute("""SELECT user_id,notifications FROM user_settings where notifications = 'ON' """)

        #Only send email to those who have opted for it
        user_ids = [row[0] for row in cur.fetchall()] 
        
        cur.close()
        print(user_ids)

        for user_id in user_ids:

            send_email(user_id=user_id)
        # Wait until midnight to avoid sending multiple emails
        tomorrow = datetime.now() + timedelta(days=1)
        midnight = datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=0, minute=0, second=0)
        time_until_midnight = (midnight - datetime.now()).total_seconds()
        print("Sleeping till midnight...")
        time.sleep(time_until_midnight)
    else:
        # Sleep for 1 hour and check again
        time.sleep(10)



