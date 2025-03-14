#!/bin/bash

count=1
cat $1 | while read line
do
    echo "Line $count : $line"
    count=$[ $count + 1 ]
done
echo "Finishing processing the file."
