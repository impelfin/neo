#!/bin/bash

echo
echo "## Stopping Oracle Listener (if running)"
lsnrctl stop || echo "Listener may not be running."

echo
echo "## Removing pre-installed oracle-xe"
rm -rf /u01
rpm -qa | grep oracle-xe && rpm -e --nodeps oracle-xe || echo "No existing oracle-xe package found."

cd ~/Disk1

echo
echo "## Installing required dependencies"
yum -y install libnsl

echo
echo "## Installing Oracle XE 11.2"
rpm -ivh --force oracle-xe-11.2.0-1.0.x86_64.rpm

echo
echo "## Configuring Oracle XE"
if [ -f "/u01/app/oracle/product/11.2.0/xe/bin/oracle_env.sh" ]; then
    . /u01/app/oracle/product/11.2.0/xe/bin/oracle_env.sh
else
    echo "Error: oracle_env.sh not found!"
    exit 1
fi

service oracle-xe configure << EOF
8080
1521
1234
1234
y
EOF

#echo
#echo "## Configuring firewall"
#firewall-cmd --permanent --add-port=8080/tcp
#firewall-cmd --permanent --add-port=1521/tcp
firewall-cmd --reload

echo
echo "## Checking listener and network status"
lsnrctl status
netstat -ntlp

echo
echo "## Install Done!!"

echo 
echo "## oracle setup"
sqlplus system/1234@xe << EOF
EXEC DBMS_XDB.SETLISTENERLOCALACCESS(FALSE);
alter user hr account unlock identified by 1234;
exit
EOF

echo 
echo "## setup Done"
