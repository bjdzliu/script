#!/bin/bash

blockip=$(grep "Failed password for" /var/log/auth.log|grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'|uniq -c|awk '{if($1>2)print $2}')
iptables -A INPUT -s $blockip  -j DROP
