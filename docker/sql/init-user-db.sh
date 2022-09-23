#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER gym_app with encrypted password 'pass';
	CREATE DATABASE gym_db;
	GRANT ALL PRIVILEGES ON DATABASE gym_db TO gym_app;
EOSQL