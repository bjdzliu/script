#!/bin/bash
####################################
#Provided for lianmeng test env deployment
#author liudz@citic.com
####################################
while true
do
case "$1" in
-s)
service=$2
shift 2
;;
-v)
version=$2
shift 2
;;
--nobuild)
buildflag=0
break
;;
--build)
buildflag=1
break
;;
esac
done

echo $version
echo $service
if [[ $buildflag = 0 ]]
then
echo "-------------- do not build docker image --------------"
else
echo "-------------- would build docker image -----------------"
fi

BASEDIR=`pwd $(dirname $0)`
CERT_PATH="${BASEDIR}/cert"
DATE=`date +%Y%m%d`
tagend=${service//-/}"testcsc"${DATE}${version}
dockerspace="registry.cn-beijing.aliyuncs.com/ywspace1"

buildimage()
{
cd ${BASEDIR}/${service}
docker build -t ${dockerspace}/zhongxinyun-test:${tagend} .
#docker push ${dockerspace}/zhongxinyun-test:${tagend}
echo $tagend

}

if [[ $buildflag = 1 ]]
then
buildimage
fi


sed  "s/REPLACETAG/${tagend}/" ${BASEDIR}/${service}/${service}.yaml > ${BASEDIR}/${service}/${service}.new.yaml
PROJECT_URL="https://master3g8.cs-cn-beijing.aliyun.com:20101/projects"
cd ${BASEDIR}/${service}
TEMPLATE=$(cat ${service}.new.yaml| awk '{printf $N"\\r\\n"}' |sed 's/\"/\\\"/g')
echo "{\"name\":\"${service}\",\"template\":\"${TEMPLATE}\", \"version\": \"${version}\"}" > ${BASEDIR}/${service}/json.txt

#curl -s -X POST -k --cert ${CERT_PATH}/cert.pem --key ${CERT_PATH}/key.pem ${PROJECT_URL}/${appname}/update -d @json.txt
