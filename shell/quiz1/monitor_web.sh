#!/bin/sh
weburl=https://developer.ibm.com/linuxone/
#weburl=http://www.google.com
logfile=/root/monitorLinuxOneSite/monitor.log

curl --connect-timeout 60 -s "$weburl" > /dev/null
if [ $? -eq 7 ] 
then
echo "Network is unreachable"
else
{
httpcode=`curl -o /dev/null -s -w %{http_code} "$weburl"`
echo $httpcode
if [ $httpcode != 200 ]
then
echo "web on linuxone is down!" | mail -s "web on linuxone is down" 1@cn.ibm.com
echo "web on linuxone is down!" | mail -s "web on linuxone is down" 2@cn.ibm.com
echo "web on linuxone is down!" | mail -s "web on linuxone is down" 3@cn.ibm.com
#echo "web is down!" 
else 
{
curl $weburl > /root/monitorLinuxOneSite/index.html
mytestfile="/root/monitorLinuxOneSite/index.html"
}
fi
}
fi

if [ -e "$mytestfile" ]
then
grep "Test drive LinuxONE and let us know what you think!" $mytestfile
if [ $? -eq 0 ] 
then
echo "web-content is checked ok! `date '+%Y-%m-%d %H:%M:%S'`" >> $logfile
else
echo "web content have error " | mail -s "web content error" 1@cn.ibm.com
echo "web content have error " | mail -s "web content error" 2@cn.ibm.com
echo "web content have error " | mail -s "web content error" 3@cn.ibm.com
#echo "web content have error "
fi
fi

if [ -e "$mytestfile" ]
then
httptime=`curl -o /dev/null -s -w "time_connect: %{time_connect}\ntime_starttransfer:%{time_starttransfer}\ntime_total: %{time_total}\n" "$weburl"|grep time_total|awk -F ":" '{print $2*1000}'`
if [ $httptime -ge 60000 ]
then
echo "web is timeout!,Response time is longer than 1min" | mail -s "WEB on linuxone Response time is longer than 1min" 1@cn.ibm.com
echo "web is timeout!,Response time is longer than 1min" | mail -s "WEB on linuxone Response time is longer than 1min" 2@cn.ibm.com
echo "web is timeout!,Response time is longer than 1min" | mail -s "WEB on linuxone Response time is longer than 1min" 3@cn.ibm.com
#echo "web is timeout!,Response time is longer than 10sec" 
else
echo "web is connect ok! at `date '+%Y-%m-%d %H:%M:%S'` RT is about $httptime " >> /root/monitorLinuxOneSite/monitor.log
fi
fi
rm $mytestfile
