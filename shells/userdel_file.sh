#!/bin/bash

input="user.dat"

while IFS=',' read -r username uid gid comment
do
    userdel "$username"
    rm -rf /home/$username
    rm -rf /var/mail/$username
    echo "Delete $username"
done < $input

echo
tail -5 /etc/passwd

