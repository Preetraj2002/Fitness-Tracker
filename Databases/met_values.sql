-- Step 1: Create Directory Object (if not already created)
CREATE OR REPLACE DIRECTORY csv_dir AS 'E:\db_proj';

-- Step 2: Drop existing tables (if they exist)
DROP TABLE met_value_table;
DROP TABLE met_value_ext;

-- Step 3: Create met_value_table
CREATE TABLE met_value_table (
    Exercise_ID NUMBER PRIMARY KEY,
    Exercise VARCHAR2(100),
    Description VARCHAR2(500),
    MET_Value NUMBER
);

-- Step 4: Create External Table for met_value.csv
CREATE TABLE met_value_ext (
    Exercise_ID NUMBER,
    Exercise VARCHAR2(100),
    Description VARCHAR2(500),
    MET_Value NUMBER
)
ORGANIZATION EXTERNAL (
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY csv_dir
    ACCESS PARAMETERS (
        RECORDS DELIMITED BY NEWLINE
        FIELDS TERMINATED BY ','
        MISSING FIELD VALUES ARE NULL
        (
            Exercise_ID,
            Exercise,
            Description,
            MET_Value FLOAT EXTERNAL
        )
    )
    LOCATION ('MET_values.csv')
)
REJECT LIMIT UNLIMITED; -- Set rejection limit as needed

-- Step 5: Insert Data from External Table into Actual Table
INSERT INTO met_value_table (Exercise_ID, Exercise, Description, MET_Value)
SELECT Exercise_ID, Exercise, Description, MET_Value
FROM met_value_ext;
