#!/bin/bash

set -e
set -u

database=$1
user=$2
url=postgresql://"$POSTGRES_USER":"$POSTGRES_PASSWORD"@"$POSTGRES_SERVER"
echo "  Connecting to PostgreSQL server at '$url'..."
echo "  Remove database '$database' and user '$user'..."
psql $url <<-EOSQL
    DROP DATABASE IF EXISTS $database;
    DROP USER IF EXISTS $user;
EOSQL