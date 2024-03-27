DROP TABLE user_settings;
-- Create user_settings table
CREATE TABLE user_settings (
    user_id NUMBER PRIMARY KEY,
    notifications VARCHAR2(3) CHECK (notifications IN ('ON', 'OFF'))
);

-- Insert the first five users with notifications set to "OFF"
INSERT INTO user_settings (user_id, notifications) VALUES (1, 'OFF');
INSERT INTO user_settings (user_id, notifications) VALUES (2, 'ON');
INSERT INTO user_settings (user_id, notifications) VALUES (3, 'OFF');
INSERT INTO user_settings (user_id, notifications) VALUES (4, 'ON');
INSERT INTO user_settings (user_id, notifications) VALUES (5, 'OFF');