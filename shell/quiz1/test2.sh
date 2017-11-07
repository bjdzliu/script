hh=123
echo $hh
for  var in `cat /tmp/names|awk '{print $1}'`
do
echo $var
if [[ ${var} = ${hh} ]];then
flag=1
else
flag=0
fi
done
echo $flag
