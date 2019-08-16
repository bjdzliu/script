# -*- coding: utf-8 -*-
"""
按照key的时间清理
参数：csv文件  key前缀

"""
import redis,re,sys
from datetime import datetime

def findkey(r,prefixkey,shortkey):
    with open(filename, 'r') as f:
        for line in f:
            str0='0,string,'+shortkey+':'
            if line.find(str0) == 0:
                try:
                   date1=line.split(",",-1)[-1].split(".",1)[0]
                   cday = datetime.strptime(date1, '%Y-%m-%dT%H:%M:%S')
                   #删除7天内过期的
                   if (cday - datetime.now()).days < 7:
                       findkey = re.findall(prefixkey, line)
                       deletekey = findkey[0].split(",")[0]
                       #print deletekey
                       r.delete(deletekey)
                except Exception :
                   pass
                continue

if __name__ == "__main__":
    pool = redis.ConnectionPool(host='address', port=6379, db=0,password='password')
    r = redis.Redis(connection_pool=pool)
    rexdict = {"u": r"u:.*?,", "cu": r"cu:.*?,"}
    filename = sys.argv[1]
    key= sys.argv[2]
    if key=="cu":
        print "cu key is",key
        findkey(r,rexdict["cu"],"cu")

    elif key=="u":
        print "key is",key
        findkey(r,rexdict["u"],"u")
    else:
        pass
    print("delete done")