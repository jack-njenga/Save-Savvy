-- This query resets the database and recreated its again
-- Warning it should only be used if only there is a serous error
-- (NOTE) ALL THE DATA IN THE DATABASE WILL BE LOST

DROP DATABASE IF EXISTS savy_db;

SOURCE ./savy.sql;
