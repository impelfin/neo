#!/bin/bash

for i in {1..100}; do
    printf "%03d %s\n" $i $(openssl rand -hex 12);
done > split-test
