#!/bin/bash
declare name=''

fun1(){
echo "input your name:"
read name
if [ $name = 'exit' ]
then
exit
fi

}

echo "------------------------------"
echo "input exit if you want to exit"
echo "------------------------------"

fun1
num=$(($RANDOM%100))
echo "$num $name" >> /tmp/names

while true
do

num=$(($RANDOM%100))
echo $num
for var in `cat /tmp/names|awk '{print $1}'`
do
if [[ ${var} = ${num} ]];then
flag=1
echo "get duplicate value" $num
else
flag=0
fi
done

if ((${flag}==0));then
fun1
echo "$num $name" >> /tmp/names
fi

done

