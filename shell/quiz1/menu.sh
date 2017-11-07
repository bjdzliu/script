#!/bin/bash
cat <<EOF
1.[install lamp]
2.[install lnmp]
3.[exit]
EOF
n=1
while [[ n -eq 1 ]]
do
echo "please your choice:"
read  input
case $input in
1)
echo "startinstalling lamp."
if [ -x /bin/ls ];then
/bin/ls
echo "lamp is installed"
else
echo "no file"
exit
fi
#/server/scripts/lamp.sh
n=0
;;
2)
echo "startinstalling lnmp."
#execute a script
echo "lnmp is installed"
n=0
;;
3)
echo "quit!"
exit
;;
?)
n=1
echo "Input error"
esac
done

