-- Creates the savvy database, user etc
CREATE DATABASE IF NOT EXISTS savy_db;
CREATE USER IF NOT EXISTS "savy_user"@"localhost" IDENTIFIED BY "Savy-2146";

GRANT ALL PRIVILEGES ON savy_db.* TO "savy_user"@"localhost";
GRANT SELECT ON performace_schema.* TO "savy_user"@"localhost";

FLUSH PRIVILEGES;
