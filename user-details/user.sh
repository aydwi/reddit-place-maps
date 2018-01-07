#!/bin/bash

f="$2.csv"

hash=`echo -n $2 | openssl dgst -binary -sha1 | openssl base64`

echo "timestamp,hash,x,y,color" > $f
grep "^[^,]\+,$hash" $1 >> $f

printf "Finished writing history of %s to file!\n\n" $2