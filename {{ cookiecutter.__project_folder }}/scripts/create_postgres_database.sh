#!/bin/bash

set -e
set -u

database=$1
user=$2
password=$3
url=postgresql://"$POSTGRES_USER":"$POSTGRES_PASSWORD"@"$POSTGRES_SERVER"
echo "  Connecting to PostgreSQL server at '$url'..."
echo "  Creating database '$database' for user '$user'..."
psql $url <<-EOSQL
  SELECT 'CREATE USER $user WITH PASSWORD ''$password'''
    WHERE NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '$user')\gexec
  SELECT 'CREATE DATABASE $database WITH OWNER = $user'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$database')\gexec
EOSQL