DROP DATABASE IF EXISTS gym_db;
CREATE USER gym_app with encrypted password 'pass';
CREATE DATABASE gym_db;
GRANT ALL PRIVILEGES ON DATABASE gym_db to gym_app;