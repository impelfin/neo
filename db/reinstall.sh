    echo
    lsnrctl stop
    echo
    echo "## delete pre-installed oracle-xe"
    rm -rf /u01
	rpm -qa | grep oracle-xe
	rpm -e oracle-xe
	cd ~/Disk1
	rpm -ivh oracle*
	
    echo
    echo "## configure oracle-xe"
    service oracle-xe configure << EOF
	8080
	1521
	1234\n
	1234\n
	y
	EOF

    echo
	lsnrctl status
	netstat -ntlp

    echo
    echo "Done!!"