#!/bin/bash

mongod --config /shard/mongoConfig.conf &
mongos --config /shard/mongoRouter.conf &
sleep 3s
mongod --config /shard/mongoShard1.conf &
mongod --config /shard/mongoShard2.conf &
sleep 2s 

ps -ef | grep mongo
sleep 3s
netstat -ntlp

