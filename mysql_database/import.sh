#!/bin/bash

docker exec --interactive mysql-server mysql -u root -pPASSWORD < ./database.sql