#!/bin/bash

cp database.sql database.bak.sql
docker exec --interactive mysql-server mysqldump -u root -pPASSWORD --databases ehr 2>/dev/null > database.sql