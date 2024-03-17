DROP TABLE SLEEP;
CREATE TABLE Sleep (
    UserID INT,
    Timestamp VARCHAR(50),
    TotalDuration DECIMAL(10, 2), -- Total sleep duration in hours
    Deep DECIMAL(10, 2), -- Deep sleep duration in hours
    Light DECIMAL(10, 2), -- Light sleep duration in hours
    Rem DECIMAL(10, 2), -- REM sleep duration in hours
    SleepQualityIndex DECIMAL(10, 2) -- Sleep quality index
);

INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
(1, '2024-01-01 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-02 23:00:00', 7, 2, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-03 23:00:00', 9, 4, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-04 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-05 23:00:00', 11, 5, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-06 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-07 23:00:00', 10, 4, 4, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-08 23:00:00', 7, 3, 2, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-09 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-10 23:00:00', 12, 5, 5, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-11 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-12 23:00:00', 9, 4, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-13 23:00:00', 7, 3, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-14 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-15 23:00:00', 10, 4, 4, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-16 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-17 23:00:00', 11, 4, 5, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-18 23:00:00', 7, 3, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-19 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-20 23:00:00', 9, 4, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-21 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-22 23:00:00', 10, 4, 4, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-23 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-24 23:00:00', 7, 2, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-25 23:00:00', 11, 4, 5, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-26 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-27 23:00:00', 9, 4, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-28 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-29 23:00:00', 12, 5, 5, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (1, '2024-01-30 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-01 23:00:00', 6, 2, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-02 23:00:00', 11, 4, 5, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-03 23:00:00', 7, 3, 3, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-04 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-05 23:00:00', 9, 4, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-06 23:00:00', 7, 2, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-07 23:00:00', 10, 4, 4, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-08 23:00:00', 12, 5, 5, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-09 23:00:00', 7, 3, 2, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-10 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-11 23:00:00', 10, 4, 4, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-12 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-13 23:00:00', 9, 4, 3, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-14 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-15 23:00:00', 8, 3, 4, 1)
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-16 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-17 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-18 23:00:00', 11, 4, 5, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-19 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-20 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-21 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-22 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-23 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-24 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-25 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-26 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-27 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-28 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-29 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (2, '2024-01-30 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
(3, '2024-01-15 23:00:00', 7, 2, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-16 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-17 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-18 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-19 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-20 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-21 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-22 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-23 23:00:00', 11, 4, 5, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-24 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-25 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-26 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-27 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-28 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-29 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-30 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-01-31 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-01 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-02 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-03 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-04 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-05 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-06 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-07 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-08 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-09 23:00:00', 11, 4, 5, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-10 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-11 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-12 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-13 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-14 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (3, '2024-02-15 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
(4, '2024-02-01 23:00:00', 7, 2, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-02 23:00:00', 10, 4, 4, 2);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-03 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-04 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    
    (4, '2024-02-05 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-06 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-07 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-08 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-09 23:00:00', 11, 4, 5, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-10 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-11 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-12 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-13 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-14 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-15 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-16 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-17 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-18 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-19 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-20 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-21 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-22 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-23 23:00:00', 11, 4, 5, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-24 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-25 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-26 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-27 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-28 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-02-29 23:00:00', 7, 3, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-03-01 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (4, '2024-03-02 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
(5, '2024-02-15 23:00:00', 8, 3, 4, 1);
INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-16 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-17 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-18 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-19 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-20 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-21 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-22 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-23 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-24 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-25 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-26 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-27 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-28 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-02-29 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-01 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-02 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-03 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-04 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-05 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-06 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-07 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-08 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-09 23:00:00', 9, 4, 3, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES     
    (5, '2024-03-10 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-11 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-12 23:00:00', 10, 4, 4, 2);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-13 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-14 23:00:00', 6, 2, 3, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-15 23:00:00', 8, 3, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-16 23:00:00', 7, 2, 4, 1);
    INSERT INTO Sleep (UserID, Timestamp, TotalDuration, Deep, Light, Rem)
VALUES 
    (5, '2024-03-17 23:00:00', 9, 4, 3, 2);
    
UPDATE Sleep
SET SleepQualityIndex = ((Deep / TotalDuration) * 2) + ((Light / TotalDuration) * 2) + ((Rem / TotalDuration) * 2);

