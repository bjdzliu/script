PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

network="172.16.30"

for sitenu in $(seq 2 254)
  do
    ping -c 1 -w 1 ${network}.${sitenu} &> /dev/null && result=0 || result=1
    if [ "$result" == 0 ];then
       echo "Server ${network}.${sitenu} is UP."
    else
       echo "Server ${network}.${sitenu} is DOWN."
    fi
  done

