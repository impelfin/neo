profile: /etc/profile
	source $^
	source ~/.bashrc
start:
	lsnrctl start
stop:
	lsnrctl stop
status:
	lsnrctl status
	netstat -ntlp
reinstall:
	rm -rf /u01
	rpm -qa | grep oracle-xe
	rpm -e oracle-xe
	cd ~/Disk1
	rpm -ivh oracle*
	service oracle-xe configure << EOF
	8080
	1521
	1234
	1234
	y
	EOF
	lsnrctl status
	netstat -ntlp
	