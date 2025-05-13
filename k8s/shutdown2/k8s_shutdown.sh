#!/bin/bash

node_user="root"
node_ip="192.168.1.211"
node_pass="1234"

echo "Shutting down K8S Node ($node_ip)..."

sshpass -p "${node_pass}" ssh -o StrictHostKeyChecking=no ${node_user}@${node_ip} "nohup shutdown -h now > /dev/null 2>&1 &"

if [ $? -eq 0 ]; then
    echo "K8S Node shut down command sent successfully."
    echo "Shutting down K8S Master..."
    sudo shutdown now
else
    echo "Failed to send shutdown command to K8S Node. Aborting shutdown of K8S Master."
fi