#!/bin/bash

f1="xyc.csv"
f2="u_xyc.csv"
f3="reqcol.csv"
f4="fin.csv"

cut -d, -f1-2 --complement $1 > $f1
sort -u $f1 > $f2

grep -P "^([\d]+,){2}$2" $f2 > $f3
#awk -v var=$2 -F, '$3 == var' $f2 > $f3

cut -d, -f3 --complement $f3 > $f4

if [ -f $f1 ] ; then
    rm $f1
fi

if [ -f $f2 ] ; then
    rm $f2
fi

if [ -f $f3 ] ; then
    rm $f3
fi