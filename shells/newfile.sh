#!/bin/bash

file1=$1
file2=$2

if [ $# -eq 2 ]; then
    if [ $file1 -nt $file2 ]; then
        echo "$file1 is newer file than $file2."
    else 
        echo "$file2 is newer file than $file1."
    fi
else    
    echo "Input two parameters...!!"
fi
    