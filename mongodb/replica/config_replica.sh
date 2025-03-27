#!/bin/bash

# Mongodb Daemon Stop
./stop_replica.sh

# Directory Setup
if [ -d /replica/data ]; then
    rm -rf /replica/data
else
    mkdir -pv /replica/data
    mkdir -pv /replica/data/master
    mkdir -pv /replica/data/slave1
    mkdir -pv /replica/data/slave2
    mkdir -pv /replica/data/arbiter

    touch /replica/data/master/master.log
    touch /replica/data/slave1/slave1.log
    touch /replica/data/slave2/slave2.log
    touch /replica/data/arbiter/arbiter.log
fi

# MongodB Daemon Start
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/master.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/slave1.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/slave2.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/arbiter.conf &
netstat -ntlp | grep mongo
sleep 3s

# Replica Init Setup
/replica/mongodb/bin/mongo --port 10000 < rs_start    
