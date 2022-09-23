#!/bin/bash

echo "=====================psql.sh================================"
echo "============================================="

docker exec -it postgres psql -U gym_app -d gym_db
