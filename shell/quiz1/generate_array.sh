#!/bin/bash
declare -new
aa=`printf "%02d " {1..100}`
echo $aa

for ((i=1;i<101;i++))
do
value=`echo  ${aa}|awk -F ' '  '{print $i}'`
new[${i}]=value
done

echo ${#new[@]}

