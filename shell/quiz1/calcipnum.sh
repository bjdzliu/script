cat 1.log | awk '{print $2}'|sort|uniq > 2.log

for ip in `cat 2.log`
do 
num=`cat 1.log|grep $ip|wc -l` 
echo "$ip $num"

done
