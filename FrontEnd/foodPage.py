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
        "Amaranth seed, Black",
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
        "Soya bean, brown",
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
        "Spinach",
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
        "Zucchini, green",
    ],
    "RootVegetables": [
        "Beetroot",
        "Carrot",
        "Potato brown",
        "Radish,white",
        "Sweet potato,brown",
        "Tapioca",
        "Yam",
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
        "Wood apple",
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
        "Turmeric powder",
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
        "Chia seeds",
    ],
    "Sugars": ["Jaggery cane", "Sugarcane, juice"],
    "MilkAndMilkProducts": [
        "Milk, whole, buffalo",
        "Milk, whole, cow",
        "Paneer",
        "Khoa",
        "Soy milk",
        "Tofu",
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
        "Pork, chops",
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
        "Squid",
    ],
    "FatsAndOils": ["Ghee", "Butter", "Oil", "Cheese"],
    "MiscellaneousFoods": [
        "Coconut water",
        "Cold Drink",
        "Chips",
        "Cakes",
        "Chocolates",
        "Sweets",
    ],
}


def calculate_calories(food, quantity):
    # Retrieve CAL/100 from FoodCalChart or some other source
    # Calculate calories using quantity and CAL/100
    # For demonstration, let's assume a fixed value for CAL/100
    cal_per_100g = 100.0  # Placeholder value, replace this with actual lookup
    calories = (quantity / 100) * cal_per_100g
    return calories


def food_calorie_tracker(user_id, conn):
    # Streamlit app layout
    st.title("Food Calorie Tracker")

    # Date input
    date = st.date_input("Select Date")

    # Time slot selection
    time_slot = st.selectbox(
        "Select Time Slot", ["9:00 AM", "1:00 PM", "5:00 PM", "9:00 PM"]
    )

    # Key selection
    category = st.selectbox("Select Category", list(hashmap.keys()))

    # Food selection
    food = st.selectbox("Select Food", hashmap[category])

    # Quantity input
    quantity = st.number_input("Enter Quantity (in g/ml)", min_value=1)

    # Submit button
    if st.button("Submit", type="primary"):
        # Calculate calories
        calories = calculate_calories(food, quantity)

        # Display result
        st.write(f"Food: {food}")
        st.write(f"Quantity: {quantity} g/ml")
        st.write(f"Calories: {calories}")
