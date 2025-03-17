#!/bin/bash

dir1=$1
dir2=$2

( cd $dir1; find . -maxdepth 1 -type f -print | sort ) > dir1-file.lst
( cd $dir2; find . -maxdepth 1 -type f -print | sort ) > dir2-file.lst

comm dir1-file.lst dir2-file.lst
