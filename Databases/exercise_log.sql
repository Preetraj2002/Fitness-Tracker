DROP TABLE exercise_log;

CREATE TABLE exercise_log (
    time_stamp TIMESTAMP,
    user_id NUMBER,
    exercise_type VARCHAR2(100),
    duration_hours NUMBER,
    calories_burnt NUMBER,
    FOREIGN KEY (user_id) REFERENCES "user" (id)
);

-- Step 1: Create Directory Object
CREATE OR REPLACE DIRECTORY csv_dir AS 'E:\db_proj';

DROP TABLE exercise_log_ext;

-- Step 2: Create External Table
CREATE TABLE exercise_log_ext (
    time_stamp TIMESTAMP,
    user_id NUMBER,
    exercise_type VARCHAR2(100),
    duration_hours NUMBER,
    calories_burnt NUMBER
)
ORGANIZATION EXTERNAL (
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY csv_dir
    ACCESS PARAMETERS (
        RECORDS DELIMITED BY NEWLINE
        FIELDS TERMINATED BY ','
        MISSING FIELD VALUES ARE NULL
        (
            time_stamp CHAR(100) DATE_FORMAT DATE MASK "YYYY-MM-DD HH24:MI:SS",
            user_id,
            exercise_type CHAR(100),
            duration_hours FLOAT EXTERNAL,
            calories_burnt FLOAT EXTERNAL
        )
    )
    LOCATION ('exercise_log.csv')
)
REJECT LIMIT UNLIMITED; -- Set rejection limit as needed

-- Step 3: Insert Data from External Table into Actual Table
INSERT INTO exercise_log (time_stamp, user_id, exercise_type, duration_hours, calories_burnt)
SELECT time_stamp, user_id, exercise_type, duration_hours, calories_burnt
FROM exercise_log_ext;

