#!/bin/bash

echo "=====================psql.sh================================"
echo "============================================="

docker exec -it postgres psql -U docker -d gym_app_db
