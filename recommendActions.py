import cx_Oracle

# Connect to your Oracle database
conn = cx_Oracle.connect("system/12345678@localhost:1521/xepdb1")


def calculate_hydration_level(daily_water_intake_ml, weight_kg):
    # Calculate optimal water intake based on body weight
    optimal_water_intake_ml = weight_kg * 35 
    # Calculate hydration level
    hydration_level = daily_water_intake_ml / optimal_water_intake_ml
    return hydration_level

def calculate_sleep_quality(sleep_data):

    # Define optimal sleep durations
    optimal_sleep_durations = {'light_sleep': 4, 'deep_sleep': 2, 'rem_sleep': 2}

    # Define weights for each sleep stage
    weights = {'light_sleep': 0.3, 'deep_sleep': 0.4, 'rem_sleep': 0.3}

    # Calculate individual scores for each sleep stage
    individual_scores = {}
    for stage, duration in optimal_sleep_durations.items():
        individual_scores[stage] = (min(duration, sleep_data[stage]) / duration) * 100

    # Calculate weighted average sleep quality score
    weighted_average_score = sum(individual_scores[stage] * weights[stage] for stage in optimal_sleep_durations) / sum(weights.values())

    # Round the sleep quality score to two decimal places
    sleep_quality = round(weighted_average_score, 2)/100

    return sleep_quality

def fetch_lowest_met_exercises(n):
    # Query to fetch exercise with the lowest MET value
    query =f"""
    SELECT Exercise, MET_Value
    FROM met_value_table
    ORDER BY MET_Value ASC
    FETCH FIRST {n} ROW ONLY
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    cursor.close()
    return result

def fetch_highest_met_exercises(n):
    # Query to fetch exercise with the highest MET value
    query =f"""
    SELECT Exercise, MET_Value
    FROM met_value_table
    ORDER BY MET_Value DESC
    FETCH FIRST {n} ROW ONLY
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    cursor.close()
    return result

def fetch_lowest_caloric_density_foods(n):
    # Query to fetch food with the lowest caloric density
    query = f"""
    SELECT FOODNAME, "CAL/100" as cal_per_100
    FROM foodcalchart
    ORDER BY cal_per_100 ASC
    FETCH FIRST {n} ROW ONLY
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    cursor.close()
    return result

def fetch_highest_caloric_foods(n):
    # Query to fetch food with the highest caloric density
    query = f"""
    SELECT FOODNAME, "CAL/100" as cal_per_100
    FROM foodcalchart
    ORDER BY cal_per_100 DESC
    FETCH FIRST {n} ROW ONLY
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    # print(result)
    cursor.close()
    return result


def generate_recommendations(data):
    recommendations = []
    

    calorie_deficit = data['calories_in_today'] - data['calories_burnt_today']
    hydration_level = calculate_hydration_level(data['water_intake_today'], data['wt'])
    sleep_quality = calculate_sleep_quality(data['sleep_data']) 


    # Generate recommendations based on analyzed data
    if calorie_deficit < 0:
        recommendations.append("You are in calorie deficit.")
        recommendations.append("If losing your weight is not the goal, consider increasing your calorie intake.")

        # Fetch foods with the highest caloric densities
        highest_caloric_density_foods = fetch_highest_caloric_foods(10)
        if highest_caloric_density_foods:
            recommendations.append("Consider these foods recommendations to increase your calorie intake:")
            for food in highest_caloric_density_foods:
                recommendations.append(f"- {food[0]}")

        # Fetch exercises with the lowest MET values
        lowest_met_exercises = fetch_lowest_met_exercises(4)
        if lowest_met_exercises:
            recommendations.append("To still enjoy the fun of exercise, consider these exercises to balance your calorie burnout (based on MET values):")
            for exercise in lowest_met_exercises:
                recommendations.append(f"- {exercise[0]}")

    elif calorie_deficit > 0:
        recommendations.append("Ensure you're burning enough calories through physical activity.")
        recommendations.append("Choose low-calorie foods to maintain a healthy diet.")

        # Fetch foods with the lowest caloric densities
        lowest_caloric_density_foods = fetch_lowest_caloric_density_foods(10)  
        if lowest_caloric_density_foods:
            recommendations.append("Choose these foods to feel full while having optimal calories:")
            for food in lowest_caloric_density_foods:
                recommendations.append(f"- {food[0]}")

        # Fetch exercises with the highest MET values
        highest_met_exercises = fetch_highest_met_exercises(4) 
        if highest_met_exercises:
            recommendations.append("Also consider these exercises to burn more calories in less time (based on MET values): ")
            for exercise in highest_met_exercises:
                recommendations.append(f"- {exercise[0]}")

    if hydration_level < 0.75:
        recommendations.append(f"Your hydration level is {hydration_level*100}% less than 75%.")
        recommendations.append("Drink more water throughout the day to stay hydrated.")

    if sleep_quality < 0.80:
        recommendations.append(f"Your sleep quality is {sleep_quality*100}% (less than 80%).")
        recommendations.append("Try to improve your sleep quality by following these tips:")
        recommendations.append("- Avoid blue light from screens before bedtime.")
        recommendations.append("- Eat a light snack before bed to promote better sleep.")
        recommendations.append("- Establish a consistent bedtime routine to signal your body it's time to sleep.")

    return recommendations

# Define the combined dictionary with nested sleep data
data = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 30,
    'wt': 75,                      # Weight in kilograms
    'ht': 180,                     # Height in centimeters
    'calories_in_today': 2500,     # Calories consumed today
    'calories_burnt_today': 3500,  # Calories burnt today
    'water_intake_today': 2000,    # Water intake today in milliliters
    'sleep_data': {
        'sleep_duration_yesterday': 7,  # Sleep duration yesterday in hours
        'light_sleep': 4,               # Light sleep duration yesterday in hours
        'deep_sleep': 2,                # Deep sleep duration yesterday in hours
        'rem_sleep': 1                  # REM sleep duration yesterday in hours
    }
}



from pprint import pprint
# pprint(generate_recommendations(data))
pprint(calculate_sleep_quality(data['sleep_data']))
pprint(calculate_hydration_level(data['water_intake_today'], data['wt']))