#!/bin/bash

opt=$1

if [ $opt == 'test' -o $opt == 'aaa' ]; then 
    echo good
else
    echo bad
fi
