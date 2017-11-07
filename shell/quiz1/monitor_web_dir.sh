#!/bin/bash
i=0
for line in `find /var/html/www/* -mmin -200`
do
filename[${i}]=$line
let i++
done

if (( ${#filename[@]} > 0 ))
echo "youe have ${#filename[@]}  files"
then
for ((i=0;i<${#filename[@]};i++))
do
echo "modified file is ${filename[$i]}"
sendfilename=${filename[$i]}
#echo "web $sendfilename is changed" | mail -s "web status" xiaoli@1.com
done
fi
