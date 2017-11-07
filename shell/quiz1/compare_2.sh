#!/bin/bash
read -p "please input two numer like 50 60:" input input2

echo $input

if (( $(echo $input2|awk '{print NF'}) > 1));then
echo "you input more nums,i will only get second"
fi
num2=$(echo $input2 |awk '{print $1}')

echo $num2

if (( $input < $num2 ));then
echo "$input is small than $num2"
elif (($input==$num2));then
echo "they are same"
else
echo "$input is great than $num2"
fi

