#!/bin/bash

master=$(ps -ef | grep 'master')
slave1=$(ps -ef | grep 'slave1')
slave2=$(ps -ef | grep 'slave2')
arbiter=$(ps -ef | grep 'arbiter')

second1=$(echo ${master} | cut -d " " -f2)
second2=$(echo ${slave1} | cut -d " " -f2)
second3=$(echo ${slave2} | cut -d " " -f2)
second4=$(echo ${arbiter} | cut -d " " -f2)

for var in $second1 $second2 $second3 $second4
do
	echo $var
	if [ -n ${var} ]; then
		result=$(kill -9 ${var})
		echo process is killed.
	else
		echo running process not found.
	fi
done	
echo
