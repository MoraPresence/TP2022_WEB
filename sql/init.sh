#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER mora;
	CREATE DATABASE catoverflow;
	GRANT ALL PRIVILEGES ON DATABASE catoverflow TO mora;
EOSQL
