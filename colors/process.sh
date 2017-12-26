#!/bin/bash

printf "Specified color index is %d \n\n" $2
printf "Processing...\n\n"

f1="xyc.csv"
f2="u_xyc.csv"
f3="reqcol.csv"

col_arr=("FFFFFF.csv" "E4E4E4.csv" "888888.csv" "222222.csv" \
"FFA7D1.csv" "E50000.csv" "E59500.csv" "A06A42.csv" \
"E5D900.csv" "94E044.csv" "02BE01.csv" "00E5F0.csv" \
"0083C7.csv" "0000EA.csv" "E04AFF.csv" "820080.csv")

f4=${col_arr[$2]}

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

printf "Finished writing file with name %s\n\n" $f4