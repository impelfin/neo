#!/bin/bash

/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/master.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/slave1.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/slave2.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/arbiter.conf &
sleep 2s

ps -ef | grep mongo
sleep 3s
netstat -ntlp | grep mongo
