DROP TABLE CerealsAndMillets;
DROP TABLE GrainLegumes;
DROP SEQUENCE GreenLeafyVegetables_ID_SEQ;
DROP TABLE GreenLeafyVegetables;
DROP TABLE OtherVegetables;
DROP SEQUENCE RootsAndTubers_ID_SEQ;
DROP TABLE RootsAndTubers;
DROP SEQUENCE Fruits_ID_SEQ;
DROP TABLE Fruits;
DROP SEQUENCE CondimentsAndSpices_ID_SEQ;
DROP TABLE CondimentsAndSpices;
DROP SEQUENCE NutsAndOilSeeds_ID_SEQ;
DROP TABLE NutsAndOilSeeds;
DROP SEQUENCE Sugars_ID_SEQ;
DROP TABLE Sugars;
DROP SEQUENCE MilkAndMilkProducts_ID_SEQ;
DROP TABLE MilkAndMilkProducts;
DROP SEQUENCE EggPoultryAndAnimalMeat_ID_SEQ;
DROP TABLE EggPoultryAndAnimalMeat;
DROP SEQUENCE FishAndSeafood_ID_SEQ;
DROP TABLE FishAndSeafood;
DROP SEQUENCE FatsAndOils_ID_SEQ;
DROP TABLE FatsAndOils;
DROP SEQUENCE MiscellaneousFoods_ID_SEQ;
DROP TABLE MiscellaneousFoods;

CREATE TABLE CerealsAndMillets (
    ID NUMBER PRIMARY KEY,
    Name VARCHAR2(100),
    Weight NUMBER(10, 2),
    Calories NUMBER(10, 2)
);
INSERT INTO CerealsAndMillets (ID, Name, Weight, Calories)
SELECT 1, 'Rice (Brown)', 100, 353.7 FROM DUAL UNION ALL
SELECT 2, 'Rice Parboiled', 100, 351.5 FROM DUAL UNION ALL
SELECT 3, 'Rice Raw milled', 100, 356.3 FROM DUAL UNION ALL
SELECT 4, 'Wheat whole', 100, 321.9 FROM DUAL UNION ALL
SELECT 5, 'Wheat flour', 100, 320.2 FROM DUAL UNION ALL
SELECT 6, 'Bulgar wheat', 100, 341.7 FROM DUAL UNION ALL
SELECT 7, 'Refined flour', 100, 351.8 FROM DUAL UNION ALL
SELECT 8, 'Ragi', 100, 320.7 FROM DUAL UNION ALL
SELECT 9, 'Rice flakes', 100, 353.7 FROM DUAL UNION ALL
SELECT 10, 'Wheat semolina', 100, 333.6 FROM DUAL UNION ALL
SELECT 11, 'Wheat vermicelli', 100, 332.6 FROM DUAL UNION ALL
SELECT 12, 'Barley', 100, 315.7 FROM DUAL UNION ALL
SELECT 13, 'Bajra', 100, 347.9 FROM DUAL UNION ALL
SELECT 14, 'Jowar', 100, 334.1 FROM DUAL UNION ALL
SELECT 15, 'Quinoa', 100, 328.3 FROM DUAL UNION ALL
SELECT 16, 'Amaranth seed, Black', 100, 356.1 FROM DUAL;


CREATE TABLE GrainLegumes (
    ID NUMBER PRIMARY KEY,
    Name VARCHAR2(100),
    Weight NUMBER(10, 2), -- Assuming weight is in grams
    Calories NUMBER(10, 2) -- Assuming calories are in kcal
);
INSERT INTO GrainLegumes (ID, Name, Weight, Calories)
SELECT 1, 'Bengal gram, dal', 100, 329.1 FROM DUAL UNION ALL
SELECT 2, 'Bengal gram, whole', 100, 287 FROM DUAL UNION ALL
SELECT 3, 'Black gram whole', 100, 291.3 FROM DUAL UNION ALL
SELECT 4, 'Cow pea, brown', 100, 320.2 FROM DUAL UNION ALL
SELECT 5, 'Cow pea, white', 100, 320.2 FROM DUAL UNION ALL
SELECT 6, 'Green gram dal', 100, 325.7 FROM DUAL UNION ALL
SELECT 7, 'Green gram, whole', 100, 293.7 FROM DUAL UNION ALL
SELECT 8, 'Horse gram, whole', 100, 329.5 FROM DUAL UNION ALL
SELECT 9, 'Lentil dal', 100, 322.4 FROM DUAL UNION ALL
SELECT 10, 'Peas, dry', 100, 303.2 FROM DUAL UNION ALL
SELECT 11, 'Rajma, red', 100, 299.2 FROM DUAL UNION ALL
SELECT 12, 'Red gram, dal', 100, 330.7 FROM DUAL UNION ALL
SELECT 13, 'Red gram, whole', 100, 273.9 FROM DUAL UNION ALL
SELECT 14, 'Soya bean, brown', 100, 381.4 FROM DUAL;

-- Create table for Green Leafy Vegetables
CREATE TABLE GreenLeafyVegetables (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE GreenLeafyVegetables_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into GreenLeafyVegetables table
INSERT INTO GreenLeafyVegetables (ID, Name, Weight, Calories)
SELECT GreenLeafyVegetables_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Amaranth leaves' AS Name, 100 AS Weight, 30.5 AS Calories FROM DUAL UNION ALL
    SELECT 'Beet greens', 100, 34.6 FROM DUAL UNION ALL
    SELECT 'Brussels sprouts', 100, 44.2 FROM DUAL UNION ALL
    SELECT 'Cabbage Chinese', 100, 17.9 FROM DUAL UNION ALL
    SELECT 'Cabbage, green', 100, 21.5 FROM DUAL UNION ALL
    SELECT 'Cauliflower leaves', 100, 35.4 FROM DUAL UNION ALL
    SELECT 'Colocasia leaves, green', 100, 43.4 FROM DUAL UNION ALL
    SELECT 'Drumstick leaves', 100, 67.3 FROM DUAL UNION ALL
    SELECT 'Fenugreek leaves', 100, 34.4 FROM DUAL UNION ALL
    SELECT 'Lettuce', 100, 21.7 FROM DUAL UNION ALL
    SELECT 'Mustard leaves', 100, 30.3 FROM DUAL UNION ALL
    SELECT 'Parsley', 100, 72.8 FROM DUAL UNION ALL
    SELECT 'Radish leaves', 100, 26.05 FROM DUAL UNION ALL
    SELECT 'Spinach', 100, 24.3 FROM DUAL
);

SELECT * from GreenLeafyVegetables;
-- Create table for Other Vegetables
CREATE TABLE OtherVegetables (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Insert data into OtherVegetables table using the DUAL table
INSERT INTO OtherVegetables (ID, Name, Weight, Calories)
SELECT 
    1, 'Ash gourd', 100, 17.4 FROM DUAL UNION ALL
SELECT 
    2, 'Bamboo shoot, tender', 100, 16.2 FROM DUAL UNION ALL
SELECT 
    3, 'Bitter gourd', 100, 20.7 FROM DUAL UNION ALL
SELECT 
    4, 'Bottle gourd', 100, 10.9 FROM DUAL UNION ALL
SELECT 
    5, 'Brinjal', 100, 25.3 FROM DUAL UNION ALL
SELECT 
    6, 'Broad beans', 100, 29.3 FROM DUAL UNION ALL
SELECT 
    7, 'Capsicum', 100, 16.2 FROM DUAL UNION ALL
SELECT 
    8, 'Cauliflower', 100, 22.9 FROM DUAL UNION ALL
SELECT 
    9, 'Celery stalk', 100, 16.4 FROM DUAL UNION ALL
SELECT 
    10, 'Cho-Cho-Marrow', 100, 18.8 FROM DUAL UNION ALL
SELECT 
    11, 'Cluster beans', 100, 40.1 FROM DUAL UNION ALL
SELECT 
    12, 'Cucumber', 100, 19.5 FROM DUAL UNION ALL
SELECT 
    13, 'French beans', 100, 24.3 FROM DUAL UNION ALL
SELECT 
    14, 'Knol-Khol', 100, 16 FROM DUAL UNION ALL
SELECT 
    15, 'Kovai', 100, 19.1 FROM DUAL UNION ALL
SELECT 
    16, 'Ladies finger', 100, 27.4 FROM DUAL UNION ALL
SELECT 
    17, 'Parwar', 100, 24.1 FROM DUAL UNION ALL
SELECT 
    18, 'Peas, fresh', 100, 81.2 FROM DUAL UNION ALL
SELECT 
    19, 'Plantain stem', 100, 39.4 FROM DUAL UNION ALL
SELECT 
    20, 'Pumpkin', 100, 23.1 FROM DUAL UNION ALL
SELECT 
    21, 'Ridge gourd', 100, 13.1 FROM DUAL UNION ALL
SELECT 
    22, 'Snake gourd', 100, 12.4 FROM DUAL UNION ALL
SELECT 
    23, 'Tomato', 100, 20.7 FROM DUAL UNION ALL
SELECT 
    24, 'Zucchini, green', 100, 20 FROM DUAL;
SELECT * from OtherVegetables;
-- Create table for Roots and Tubers
CREATE TABLE RootsAndTubers (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE RootsAndTubers_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into RootsAndTubers table
INSERT INTO RootsAndTubers (ID, Name, Weight, Calories)
SELECT RootsAndTubers_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Beetroot' AS Name, 100 AS Weight, 35.6 AS Calories FROM DUAL UNION ALL
    SELECT 'Carrot', 100, 33.2 FROM DUAL UNION ALL
    SELECT 'Potato brown', 100, 69.7 FROM DUAL UNION ALL
    SELECT 'Radish,white', 100, 32.2 FROM DUAL UNION ALL
    SELECT 'Sweet potato,brown', 100, 108.9 FROM DUAL UNION ALL
    SELECT 'Tapioca', 100, 79.8 FROM DUAL UNION ALL
    SELECT 'Yam', 100, 84.3 FROM DUAL
);
SELECT * from RootsAndTubers;
-- Create table for Fruits
CREATE TABLE Fruits (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE Fruits_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into Fruits table
INSERT INTO Fruits (ID, Name, Weight, Calories)
SELECT Fruits_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Apple' AS Name, 100 AS Weight, 62.3 AS Calories FROM DUAL UNION ALL
    SELECT 'Apricot, dried', 100, 31.5 FROM DUAL UNION ALL
    SELECT 'Avocado', 100, 144.3 FROM DUAL UNION ALL
    SELECT 'Banana', 100, 110.6 FROM DUAL UNION ALL
    SELECT 'Blackberry fruit', 100, 54.2 FROM DUAL UNION ALL
    SELECT 'Cherries red', 100, 59.7 FROM DUAL UNION ALL
    SELECT 'Blackcurrants', 100, 54.2 FROM DUAL UNION ALL
    SELECT 'Custard apple', 100, 98.9 FROM DUAL UNION ALL
    SELECT 'Dates, dry', 100, 320.2 FROM DUAL UNION ALL
    SELECT 'Fig', 100, 81.5 FROM DUAL UNION ALL
    SELECT 'Grapes', 100, 60.7 FROM DUAL UNION ALL
    SELECT 'Guava', 100, 32.2 FROM DUAL UNION ALL
    SELECT 'Jack fruit', 100, 72.1 FROM DUAL UNION ALL
    SELECT 'Sweet lime', 100, 27.2 FROM DUAL UNION ALL
    SELECT 'Litchi', 100, 53.7 FROM DUAL UNION ALL
    SELECT 'Mango', 100, 41.8 FROM DUAL UNION ALL
    SELECT 'Musk melon', 100, 23.1 FROM DUAL UNION ALL
    SELECT 'Orange', 100, 37.2 FROM DUAL UNION ALL
    SELECT 'Papaya', 100, 23.9 FROM DUAL UNION ALL
    SELECT 'Peach', 100, 40.1 FROM DUAL UNION ALL
    SELECT 'Pear', 100, 37.5 FROM DUAL UNION ALL
    SELECT 'Pineapple', 100, 43 FROM DUAL UNION ALL
    SELECT 'Plum', 100, 56.8 FROM DUAL UNION ALL
    SELECT 'Pomegranate', 100, 54.7 FROM DUAL UNION ALL
    SELECT 'Raisins, black', 100, 305.6 FROM DUAL UNION ALL
    SELECT 'Sapota', 100, 73.3 FROM DUAL UNION ALL
    SELECT 'Strawberry', 100, 24.6 FROM DUAL UNION ALL
    SELECT 'Watermelon', 100, 20.3 FROM DUAL UNION ALL
    SELECT 'Wood apple', 100, 78.1 FROM DUAL
);
-- Create table for Condiments and Spices
CREATE TABLE CondimentsAndSpices (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE CondimentsAndSpices_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into CondimentsAndSpices table
INSERT INTO CondimentsAndSpices (ID, Name, Weight, Calories)
SELECT CondimentsAndSpices_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Green chillies' AS Name, 100 AS Weight, 45.6 AS Calories FROM DUAL UNION ALL
    SELECT 'Coriander seeds', 100, 268.8 FROM DUAL UNION ALL
    SELECT 'Curry leaves', 100, 63.5 FROM DUAL UNION ALL
    SELECT 'Garlic', 100, 123.8 FROM DUAL UNION ALL
    SELECT 'Ginger, fresh', 100, 54.9 FROM DUAL UNION ALL
    SELECT 'Mint leaves', 100, 37 FROM DUAL UNION ALL
    SELECT 'Onion', 100, 48 FROM DUAL UNION ALL
    SELECT 'Asafoetida', 100, 331.5 FROM DUAL UNION ALL
    SELECT 'Cardamom, green', 100, 255 FROM DUAL UNION ALL
    SELECT 'Red chillies', 100, 236.6 FROM DUAL UNION ALL
    SELECT 'Cloves', 100, 186.6 FROM DUAL UNION ALL
    SELECT 'Cumin seeds', 100, 304.4 FROM DUAL UNION ALL
    SELECT 'Black cumin (Kalonji)', 100, 345 FROM DUAL UNION ALL
    SELECT 'Fenugreek seeds', 100, 234.9 FROM DUAL UNION ALL
    SELECT 'Nutmeg', 100, 463.6 FROM DUAL UNION ALL
    SELECT 'Basil seeds', 100, 22 FROM DUAL UNION ALL
    SELECT 'Anise seeds', 100, 153.3 FROM DUAL UNION ALL
    SELECT 'Pepper, black', 100, 217.4 FROM DUAL UNION ALL
    SELECT 'Poppy seeds', 100, 422.5 FROM DUAL UNION ALL
    SELECT 'Turmeric powder', 100, 280.5 FROM DUAL
);
-- Create table for Nuts and Oil seeds
CREATE TABLE NutsAndOilSeeds (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE NutsAndOilSeeds_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into NutsAndOilSeeds table
INSERT INTO NutsAndOilSeeds (ID, Name, Weight, Calories)
SELECT NutsAndOilSeeds_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Almond' AS Name, 100 AS Weight, 609.2 AS Calories FROM DUAL UNION ALL
    SELECT 'Arecanut dried', 100, 350.6 FROM DUAL UNION ALL
    SELECT 'Cashew nut', 100, 582.6 FROM DUAL UNION ALL
    SELECT 'Coconut dry', 100, 624 FROM DUAL UNION ALL
    SELECT 'Coconut fresh', 100, 408.9 FROM DUAL UNION ALL
    SELECT 'Gingelly seeds', 100, 507.6 FROM DUAL UNION ALL
    SELECT 'Ground nut', 100, 520 FROM DUAL UNION ALL
    SELECT 'Linseeds', 100, 443.8 FROM DUAL UNION ALL
    SELECT 'Pine seed', 100, 594.1 FROM DUAL UNION ALL
    SELECT 'Pistachio nuts', 100, 539.4 FROM DUAL UNION ALL
    SELECT 'Sunflower seeds', 100, 586.2 FROM DUAL UNION ALL
    SELECT 'Walnut', 100, 671 FROM DUAL UNION ALL
    SELECT 'Flax seeds', 100, 534 FROM DUAL UNION ALL
    SELECT 'Chia seeds', 100, 486 FROM DUAL
);

-- Create table for Sugars
CREATE TABLE Sugars (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE Sugars_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into Sugars table
INSERT INTO Sugars (ID, Name, Weight, Calories)
SELECT Sugars_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Jaggery cane' AS Name, 100 AS Weight, 353.7 AS Calories FROM DUAL UNION ALL
    SELECT 'Sugarcane, juice', 100, 57.8 FROM DUAL
);

-- Create table for Milk and Milk Products
CREATE TABLE MilkAndMilkProducts (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE MilkAndMilkProducts_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into MilkAndMilkProducts table
INSERT INTO MilkAndMilkProducts (ID, Name, Weight, Calories)
SELECT MilkAndMilkProducts_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Milk, whole, buffalo' AS Name, 100 AS Weight, 107.3 AS Calories FROM DUAL UNION ALL
    SELECT 'Milk, whole, cow', 100, 72.8 FROM DUAL UNION ALL
    SELECT 'Paneer', 100, 257.8 FROM DUAL UNION ALL
    SELECT 'Khoa', 100, 315.9 FROM DUAL UNION ALL
    SELECT 'Soy milk', 100, 54 FROM DUAL UNION ALL
    SELECT 'Tofu', 100, 76 FROM DUAL
);
-- Create table for Egg, Poultry, and Animal Meat
CREATE TABLE EggPoultryAndAnimalMeat (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Create sequence for ID generation
CREATE SEQUENCE EggPoultryAndAnimalMeat_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Insert data into EggPoultryAndAnimalMeat table
INSERT INTO EggPoultryAndAnimalMeat (ID, Name, Weight, Calories)
SELECT EggPoultryAndAnimalMeat_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Egg, whole, raw' AS Name, 100 AS Weight, 134.7 AS Calories FROM DUAL UNION ALL
    SELECT 'Egg white, raw', 100, 44.6 FROM DUAL UNION ALL
    SELECT 'Egg, yolk, raw', 100, 296.8 FROM DUAL UNION ALL
    SELECT 'Chicken, leg, skinless', 100, 383.6 FROM DUAL UNION ALL
    SELECT 'Chicken, thigh, skinless', 100, 199.8 FROM DUAL UNION ALL
    SELECT 'Chicken, breast, skinless', 100, 168.2 FROM DUAL UNION ALL
    SELECT 'Chicken, liver', 100, 123.8 FROM DUAL UNION ALL
    SELECT 'Goat', 100, 188 FROM DUAL UNION ALL
    SELECT 'Sheep, shoulder', 100, 200.7 FROM DUAL UNION ALL
    SELECT 'Sheep, chops', 100, 118.5 FROM DUAL UNION ALL
    SELECT 'Beef, chops', 100, 139.8 FROM DUAL UNION ALL
    SELECT 'Pork, shoulder', 100, 237.3 FROM DUAL UNION ALL
    SELECT 'Pork, chops', 100, 178.7 FROM DUAL
);
-- Create sequence for ID generation
CREATE SEQUENCE FishAndSeafood_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Create table for Fish and Seafood
CREATE TABLE FishAndSeafood (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Insert data into FishAndSeafood table using the sequence and DUAL
INSERT INTO FishAndSeafood (ID, Name, Weight, Calories)
SELECT FishAndSeafood_ID_SEQ.nextval, Name, Weight, Calories
FROM (
    SELECT 'Cat fish' AS Name, 100 AS Weight, 108.9 AS Calories FROM DUAL UNION ALL
    SELECT 'Mackerel', 100, 101 FROM DUAL UNION ALL
    SELECT 'Matha', 100, 92.9 FROM DUAL UNION ALL
    SELECT 'Pomfret', 100, 123 FROM DUAL UNION ALL
    SELECT 'Salmon', 100, 172.3 FROM DUAL UNION ALL
    SELECT 'Sardine', 100, 152.2 FROM DUAL UNION ALL
    SELECT 'Shark', 100, 95.1 FROM DUAL UNION ALL
    SELECT 'Silver fish', 100, 132.6 FROM DUAL UNION ALL
    SELECT 'Catla', 100, 94.1 FROM DUAL UNION ALL
    SELECT 'Tuna', 100, 112.3 FROM DUAL UNION ALL
    SELECT 'Crab', 100, 81.9 FROM DUAL UNION ALL
    SELECT 'Lobster', 100, 89.6 FROM DUAL UNION ALL
    SELECT 'Oyster', 100, 60.2 FROM DUAL UNION ALL
    SELECT 'Tiger prawns', 100, 65.2 FROM DUAL UNION ALL
    SELECT 'Clam', 100, 58 FROM DUAL UNION ALL
    SELECT 'Squid', 100, 80 FROM DUAL
);

-- Create sequence for ID generation for FatsAndOils table
CREATE SEQUENCE FatsAndOils_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Create table for Fats and Oils
CREATE TABLE FatsAndOils (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Insert data into FatsAndOils table using the sequence
INSERT INTO FatsAndOils (ID, Name, Weight, Calories)
SELECT FatsAndOils_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Ghee' AS Name, 100 AS Weight, 920 AS Calories FROM DUAL UNION ALL
    SELECT 'Butter', 100, 717 FROM DUAL UNION ALL
    SELECT 'Oil', 100, 900 FROM DUAL UNION ALL
    SELECT 'Cheese', 100, 264.5 FROM DUAL
);

-- Create sequence for ID generation for MiscellaneousFoods table
CREATE SEQUENCE MiscellaneousFoods_ID_SEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Create table for Miscellaneous Foods including brand information
CREATE TABLE MiscellaneousFoods (
    ID INT PRIMARY KEY,
    Name VARCHAR2(100),
    Weight DECIMAL(10, 2),
    Calories DECIMAL(10, 2)
);

-- Insert data into MiscellaneousFoods table including sweets
INSERT INTO MiscellaneousFoods (ID, Name, Weight, Calories)
SELECT MiscellaneousFoods_ID_SEQ.nextval, Name, Weight, Calories FROM (
    SELECT 'Coconut water' AS Name, 100 AS Weight, 15.2 AS Calories FROM DUAL UNION ALL
    SELECT 'Cold Drink', 100, 100 FROM DUAL UNION ALL
    SELECT 'Chips', 100, 200 FROM DUAL UNION ALL
    SELECT 'Cakes', 100, 300 FROM DUAL UNION ALL
    SELECT 'Chocolates', 100, 400 FROM DUAL UNION ALL
    SELECT 'Sweets', 100, 250 FROM DUAL
);


SELECT * FROM CerealsAndMillets;
SELECT * FROM GrainLegumes;
SELECT * FROM GreenLeafyVegetables;
SELECT * FROM OtherVegetables;
SELECT * FROM RootsAndTubers;
SELECT * FROM Fruits;
SELECT * FROM CondimentsAndSpices;
SELECT * FROM NutsAndOilSeeds;
SELECT * FROM Sugars;
SELECT * FROM MilkAndMilkProducts;
SELECT * FROM EggPoultryAndAnimalMeat;
SELECT * FROM FishAndSeafood;
SELECT * FROM FatsAndOils;
SELECT * FROM MiscellaneousFoods;
