#!/bin/bash

#This shell script generates the csv file required by 'plot.py' from the main csv file

f1="tmpfile1.csv"
f2="tmpfile2.csv"
f3="tmpfile3.csv"
f4="tmpfile4.csv"
f5="tmpfile5.csv"
f6="tmpfile6.csv"
f7="tmpfile7.csv"

f8="processed.csv"

#Remove unnecessary columns 1, 2 and 5 from the main csv file
cut -d, -f1-2,5 --complement $1 > $f1
echo "Step 1 finished"

#Merge all duplicate coordinates, and create a column containing no. of placements
python3 addcount.py
echo "Step 2 finished"

#Handling coordinates with 0 placements

#Part1 - Generate a file with all the coordinates
python3 milpair.py
echo "Step 3.1 finished"

#Step2 - Reduce original coordinates to unique values
sort -u $f1 > $f3
echo "Step 3.2 finished"

#Step3 - Find the coordinates with 0 placements
grep -F -x -v -f $f3 $f2 > $f5
echo "Step 3.3 finished"

#Step4 - Add a column of '1' to such points

#'1' is added as the count value, bacause at later steps, a logarithmic (base 10)
#function is used to normalize the count, and these values get converted to 0

python3 addone.py
echo "Step 3.4 finished"

#Merge the 2 files containing coordinates with placements and without placements
cat $f4 $f6 > $f7
echo "Step 4 finished"

#Sort the coordinates for readability
sort --field-separator=',' -n -k 1,1 -k 2,2 $f7 > $f8
echo "Step 5 finished"

#Add a header field (required for later processing)
sed -i 1i"x,y,value" $f8
echo "Step 6 finished"

#Removing intermediate files
if [ -f $f1 ] ; then
    rm $f1
fi

if [ -f $f2 ] ; then
    rm $f2
fi

if [ -f $f3 ] ; then
    rm $f3
fi

if [ -f $f4 ] ; then
    rm $f4
fi

if [ -f $f5 ] ; then
    rm $f5
fi

if [ -f $f6 ] ; then
    rm $f6
fi

if [ -f $f7 ] ; then
    rm $f7
fi

#File is ready to be passed to Python script for plotting
echo
printf "Created the required file with name %s\n\n" $f8