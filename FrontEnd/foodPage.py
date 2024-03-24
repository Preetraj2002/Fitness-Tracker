import streamlit as st

hashmap = {
    "CerealsAndMillets": [
        "Rice (Brown)",
        "Rice Parboiled",
        "Rice Raw milled",
        "Wheat whole",
        "Wheat flour",
        "Bulgar wheat",
        "Refined flour",
        "Ragi",
        "Rice flakes",
        "Wheat semolina",
        "Wheat vermicelli",
        "Barley",
        "Bajra",
        "Jowar",
        "Quinoa",
        "Amaranth seed, Black"
    ],
    "GrainLegumes": [
        "Bengal gram, dal",
        "Bengal gram, whole",
        "Black gram whole",
        "Cow pea, brown",
        "Cow pea, white",
        "Green gram dal",
        "Green gram, whole",
        "Horse gram, whole",
        "Lentil dal",
        "Peas, dry",
        "Rajma, red",
        "Red gram, dal",
        "Red gram, whole",
        "Soya bean, brown"
    ],
     "GreenLeafyVegetables": [
        "Amaranth leaves",
        "Beet greens",
        "Brussels sprouts",
        "Cabbage Chinese",
        "Cabbage, green",
        "Cauliflower leaves",
        "Colocasia leaves, green",
        "Drumstick leaves",
        "Fenugreek leaves",
        "Lettuce",
        "Mustard leaves",
        "Parsley",
        "Radish leaves",
        "Spinach"
    ],
     "OtherVegetables": [
        "Ash gourd",
        "Bamboo shoot, tender",
        "Bitter gourd",
        "Bottle gourd",
        "Brinjal",
        "Broad beans",
        "Capsicum",
        "Cauliflower",
        "Celery stalk",
        "Cho-Cho-Marrow",
        "Cluster beans",
        "Cucumber",
        "French beans",
        "Knol-Khol",
        "Kovai",
        "Ladies finger",
        "Parwar",
        "Peas, fresh",
        "Plantain stem",
        "Pumpkin",
        "Ridge gourd",
        "Snake gourd",
        "Tomato",
        "Zucchini, green"
    ],
    "RootVegetables": [
        "Beetroot",
        "Carrot",
        "Potato brown",
        "Radish,white",
        "Sweet potato,brown",
        "Tapioca",
        "Yam"
    ],
    "Fruits": [
        "Apple",
        "Apricot, dried",
        "Avocado",
        "Banana",
        "Blackberry fruit",
        "Cherries red",
        "Blackcurrants",
        "Custard apple",
        "Dates, dry",
        "Fig",
        "Grapes",
        "Guava",
        "Jack fruit",
        "Sweet lime",
        "Litchi",
        "Mango",
        "Musk melon",
        "Orange",
        "Papaya",
        "Peach",
        "Pear",
        "Pineapple",
        "Plum",
        "Pomegranate",
        "Raisins, black",
        "Sapota",
        "Strawberry",
        "Watermelon",
        "Wood apple"
    ],
     "CondimentsAndSpices": [
        "Green chillies",
        "Coriander seeds",
        "Curry leaves",
        "Garlic",
        "Ginger, fresh",
        "Mint leaves",
        "Onion",
        "Asafoetida",
        "Cardamom, green",
        "Red chillies",
        "Cloves",
        "Cumin seeds",
        "Black cumin (Kalonji)",
        "Fenugreek seeds",
        "Nutmeg",
        "Basil seeds",
        "Anise seeds",
        "Pepper, black",
        "Poppy seeds",
        "Turmeric powder"
    ],
    "NutsAndOilSeeds": [
        "Almond",
        "Arecanut dried",
        "Cashew nut",
        "Coconut dry",
        "Coconut fresh",
        "Gingelly seeds",
        "Ground nut",
        "Linseeds",
        "Pine seed",
        "Pistachio nuts",
        "Sunflower seeds",
        "Walnut",
        "Flax seeds",
        "Chia seeds"
    ],
    "Sugars": [
        "Jaggery cane",
        "Sugarcane, juice"
    ],
    "MilkAndMilkProducts": [
        "Milk, whole, buffalo",
        "Milk, whole, cow",
        "Paneer",
        "Khoa",
        "Soy milk",
        "Tofu"
    ],
    "EggPoultryAndAnimalMeat": [
        "Egg, whole, raw",
        "Egg white, raw",
        "Egg, yolk, raw",
        "Chicken, leg, skinless",
        "Chicken, thigh, skinless",
        "Chicken, breast, skinless",
        "Chicken, liver",
        "Goat",
        "Sheep, shoulder",
        "Sheep, chops",
        "Beef, chops",
        "Pork, shoulder",
        "Pork, chops"
    ],
    "FishAndSeafood": [
        "Cat fish",
        "Mackerel",
        "Matha",
        "Pomfret",
        "Salmon",
        "Sardine",
        "Shark",
        "Silver fish",
        "Catla",
        "Tuna",
        "Crab",
        "Lobster",
        "Oyster",
        "Tiger prawns",
        "Clam",
        "Squid"
    ],
    "FatsAndOils": [
        "Ghee",
        "Butter",
        "Oil",
        "Cheese"
    ],
    "MiscellaneousFoods": [
        "Coconut water",
        "Cold Drink",
        "Chips",
        "Cakes",
        "Chocolates",
        "Sweets"
    ]}

def insert_food_intake(conn, user_id, time_stamp, food_category, food, quantity):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO FOODLOG (UserID, Timestamp, FoodCategory, Food, Quantity) VALUES (:user_id, :time_stamp, :foodCategory, :food, :quantity)",
        {"user_id": user_id, "time_stamp": time_stamp, "foodCategory": food_category, "food": food, "quantity": quantity},
    )
    conn.commit()
    cur.close()

def food_calorie_tracker(user_id, conn):
    
    # Streamlit app layout
    st.title("Food Calorie Tracker")
    
    # Date input
    selected_date = st.date_input("Select Date")
    
    # Time slot selection
    selected_time = st.selectbox("Select Time Slot", ['9:00 AM', '1:00 PM', '5:00 PM', '9:00 PM'])
    
    # Key selection
    category = st.selectbox("Select Category", list(hashmap.keys()))
    
    # Food selection
    food = st.selectbox("Select Food", hashmap[category])
    
    # Quantity input
    quantity = st.number_input("Enter Quantity (in g/ml)", min_value=1)
    
    if st.button("Submit"):
        # Insert food intake into database
        time_stamp = f"{selected_date} {selected_time}"
        insert_food_intake(conn, user_id, time_stamp, category, food, quantity)

        cur = conn.cursor()
        cur.execute(
            "SELECT Calories FROM FOODLOG WHERE UserID = :user_id AND Timestamp = :time_stamp",
            {"user_id": user_id, "time_stamp": time_stamp}
        )
        calories = cur.fetchall()  # Fetch the calorie value
        st.write(f"{calories} consumed")
        cur.close()

          
