#!/bin/bash
var="I am oldboy teacher welcome to oldboy training class."
for var1 in `echo $var  |awk  '{print $0}'`
do
if (( $(expr length $var1)>6 ));then
echo $var1
fi
done

