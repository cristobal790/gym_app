#!/bin/bash

echo "=====================psql.sh================================"
echo "============================================="

docker exec -it postgres psql -U docker -d myra_rec_db
