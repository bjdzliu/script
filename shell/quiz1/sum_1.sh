#!/bin/bash
while getopts "a:b:" arg
do
case $arg in 
a)
num1=$OPTARG
;;
b)
num2=$OPTARG
;;
?)
echo "unknow argument"
exit 1
;;
esac
		
done

#pan duan num
if [ -n "`echo ${num1}|sed -n '/^[0-9]*$/p'`" ];then

echo "$num1 is number" 
else
echo "$num1 isn't a number"
exit
fi

if [ -n "`echo ${num2}|sed -n '/^[0-9]*$/p'`" ];then

echo "$num2 is number"
else
echo "$num2 isn't a number"
exit
fi



let sum=$num1+$num2
echo $sum
