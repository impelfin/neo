#!/bin/bash

a=1

while [ $a != "0" ]; do
    echo -n "Input(0:Exit) : "
    read a

    if [ $a != "0" ]; then
        for ((k=1;k<=9;k++)) do  
            echo "$a * $k = `expr $a \* $k `"
        done
    fi
done
echo Exit
