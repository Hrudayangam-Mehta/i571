#!/bin/sh

#sets dir to directory containing this script
dir=`dirname $0`

#use $dir/ as prefix to run any programs in this dir
python $dir/pysoltry1.py 
#so that this script can be run from any directory.


