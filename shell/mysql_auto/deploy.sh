#!/bin/bash
# Filename:    deploysql.sh
# Revision:    0.1
# Date:        2017/01/27
# Author:      liudz
# Parameters:
#              db host: -h <IP or HostName>
#              db user: -u root  
#              db password: -p  <password> 
#              db's port: -port <3306>
#              database's name: -d <dbname>
#              imported sql file: -f <xxx.sql>
#set -x
set -eo pipefail

currentdate=$(date -u +'%m%d')
scriptpath=$(cd `dirname $0`; pwd)

while getopts "u:p:x:d:h:f:" arg
do
      case $arg in
        u)
          user=$OPTARG
          ;;
        p)
          password=$OPTARG
          ;;
        x)
           port=$OPTARG
           ;;
        d)
           dbname=$OPTARG
           ;;
         h)
           dbhost=$OPTARG
           ;;
         f)
           sqlfile=$OPTARG
           ;;
          ?)
           echo "unkonw argument"
           exit 1
           ;;
      esac
done

#set default value
port=${port:-"3306"}
user=${user:-"root"}


input_info(){
echo "#db's name is: " $dbname
echo "#db's host is: " $dbhost
echo "#db's user  is: " $user
echo "#sql flle name is: " $sqlfile
echo "#sql port: " $port

}
input_info

#Create db backup store path
test  -d ${scriptpath}/${dbname}/${currentdate} ||  mkdir -p ${scriptpath}/${dbname}/${currentdate}
storepath=${scriptpath}/${dbname}/${currentdate}




generateTempSql(){
echo "*********** start generating the tmp.sql from  the provided sql file"
echo "*********** only get the DDL&DML phrases"
cat ${sqlfile} |grep -E "(^INSERT INTO|^insert into|^DELETE FROM|^delete from|^UPDATE|^update|^ALTER|^alter)" |sed  "s/^UPDATE\|^update/yyy &/" |sort -t ' ' -k3 > ${storepath}/update.sql
echo "*********** end generate tmp sql"
}

read -p "please confirm your info [y/n]: " input
if [[ $input == 'y' ]] 
then
generateTempSql
else
echo "exit generate temp sql"
exit 5
fi

backupTable(){
for s in $(cat ${storepath}/update.sql | awk -F' ' '{print $3}'|awk -F';' '{print $1}'| sort -u|sed 's/`//g')
do
mysqldump -h 127.0.0.1 -u root -ppassword tests1  $s > ${storepath}/$s.backup.sql
done
}

updateTables(){
read -p "please confirm whether update or now [y/n]: " input
if [[ $input == 'y' ]]
then
sed  -i "s/^UPDATE\|^update/yyy &/" ${storepath}/update.sql
mysql -h 127.0.0.1 -u root -ppassword tests1  < ${storepath}/update.sql |tee update.555.sql
else
echo "exit when ready to update tables on step execute the upgrade sql"
exit 6
fi
}

# lock specify the table  when update. Need two parameters update.sql and tables name
# $1 is update.sql and $2 is table name
insertlocktable(){
firstline=$(cat $1 | grep -n $2 |sed -n '1p'|cut -d: -f1)
sed -i "$firstline i LOCK TABLES $2 WRITE;" $1

lastline=$(cat $1 | grep -n $2|sed -n '$p'|cut -d: -f1)
sed -i "$lastline a UNLOCK TABLES;" $1

}

locktable(){
for table in `cat ${storepath}/update.sql | awk -F' ' '{print $3}'|awk -F';' '{print $1}'| sort -u `
do
insertlocktable ${storepath}/update.sql $table

done
}




cat <<EOF
You have three choices:
1.[It's your first time to backup tables]
2.[skip the backup and execute the update.sql directly]
3.[cancle the this backup&update operation]
EOF


echo "please your choice:"
read  input
case $input in
1)

echo "*********** start to backup tables"
read -p "backup your tables in the $dbname ? [y/n]: " skip
if [[ $skip == 'n' ]];then
echo "cancle the this backup"
echo "you could check and modify the update.sql as you wish"
exit
  elif [[ $skip == 'y' ]];then
#set +e
    backupTable
#set -e
else 
echo "invalid option and exit"
exit 9
fi
echo "***********  End backup tables"

echo "********** insert lock phrase"

locktable

echo "********** End insert lock phrase"

echo "************ Now  start to update tables"
updateTables
if [[ $? == '0' ]];then
echo "success"
else
echo "check update.sql"
fi
;;
2)
echo "now  start update tables"
updateTables
if [[ $? == '0' ]];then
echo "success"
else
echo "check update.sql"
fi
;;
3)
echo "cancle the backup"
exit 
;;
*)
echo "Input error"
exit 99
esac

