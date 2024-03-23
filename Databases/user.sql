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

SELECT id from "user"  WHERE username = 'psingh'  AND password = 'pqrs';