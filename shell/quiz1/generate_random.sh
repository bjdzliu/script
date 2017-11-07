#!/bin/bash
mydir=$(dirname $0)
cd $mydir
generate()
{
i=0
while [[ i -le 10 ]]
do
c=$(cat /dev/urandom | tr -dc 'a-fA-F0-9'|head -c 10)_oldboy.html
touch  $c
let "i++"
done
}

generate
