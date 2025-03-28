#!/bin/bash

echo
echo "## Database Data Import"
sqlplus system/1234@xe < shop_user_create.sql
sqlplus system/1234@xe < shop_membertbl.sql
sqlplus system/1234@xe < shop_producttbl.sql
sqlplus system/1234@xe < shop_usertbl.sql
sqlplus system/1234@xe < shop_buytbl.sql
sqlplus system/1234@xe < hr_usertbl.sql
sqlplus system/1234@xe < hr_buytbl.sql
echo
echo "Database Data Import Done"
