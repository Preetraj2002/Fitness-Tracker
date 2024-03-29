DROP TABLE "user";

CREATE TABLE "user" (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(255),
    sex VARCHAR2(10),
    age NUMBER,
    weight_kg NUMBER,
    height_cm NUMBER,
    bmi NUMBER
);

ALTER TABLE "user"
ADD username VARCHAR(255);
ALTER TABLE "user"
ADD password VARCHAR(255);

CREATE OR REPLACE TRIGGER calculate_bmi
BEFORE INSERT OR UPDATE OF weight_kg, height_cm ON "user"
FOR EACH ROW
BEGIN
    :NEW.bmi := ROUND(:NEW.weight_kg / POWER(:NEW.height_cm / 100, 2), 2);
END;
/



INSERT INTO "user" (id, name, sex, age, weight_kg, height_cm)
VALUES
(1, 'Priya Singh', 'Female', 25, 45, 165);

INSERT INTO "user" (id, name, sex, age, weight_kg, height_cm)
VALUES
(2, 'Rohan Roy', 'Male', 40, 90, 180);

INSERT INTO "user" (id, name, sex, age, weight_kg, height_cm)
VALUES
(3, 'Sakshi Desai', 'Female', 50, 55, 160);

INSERT INTO "user" (id, name, sex, age, weight_kg, height_cm)
VALUES
(4, 'Vinay Rai', 'Male', 35, 85, 175);

INSERT INTO "user" (id, name, sex, age, weight_kg, height_cm)
VALUES
(5, 'Aarti Roy', 'Female', 20, 60, 170);

INSERT INTO "user" ( id, name, sex, age, weight_kg, height_cm)
VALUES
(6,'Aarohi Roy', 'Female', 25, 60, 170);

SELECT id from "user"  WHERE username = 'psingh'  AND password = 'pqr';

UPDATE "user" SET username = 'psingh', password = 'pqr' WHERE id = 1;
UPDATE "user" SET username = 'rohan123', password = '1234' WHERE id = 2;
UPDATE "user" SET username = 'sdesai', password = '5678' WHERE id = 3;
UPDATE "user" SET username = 'vinay123', password = 'abcd' WHERE id = 4;
UPDATE "user" SET username = 'aroy123', password = 'aroy' WHERE id = 5;
UPDATE "user" SET username = 'aroy1234', password = 'aroy1' WHERE id = 6;

CREATE SEQUENCE user_id_seq
  START WITH 6
  INCREMENT BY 1
  NOCACHE
  NOCYCLE;

CREATE OR REPLACE TRIGGER user_id_trigger
BEFORE INSERT ON "user"
FOR EACH ROW
BEGIN
  SELECT user_id_seq.NEXTVAL
  INTO :new.id
  FROM dual;
END;
/

CREATE OR REPLACE PROCEDURE delete_user_and_related_entries(user_id_param IN "user".id%TYPE) IS
BEGIN
    -- Delete from water_intake
    DELETE FROM water_intake WHERE water_intake.user_id = user_id_param;

    -- Delete from sleep
    DELETE FROM sleep WHERE UserID = user_id_param;

    -- Delete from foodlog
    DELETE FROM foodlog WHERE UserID = user_id_param;

    -- Delete from exercise_log
    DELETE FROM exercise_log WHERE exercise_log.user_id = user_id_param;

    -- Delete from user
    DELETE FROM "user" WHERE id = user_id_param;
END delete_user_and_related_entries;
/

BEGIN
    delete_user_and_related_entries(6); -- Assuming the user's id is 1
END;
/




