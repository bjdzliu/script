# -*- coding: utf-8 -*-
"""
nohup python delete_key.py lmprod7.csv 2>&1 > lmprod07.nohup &


"""
import redis,re,sys

def findkey(r,rex):
    with open('lmprod5.csv', 'r') as f:
        for line in f:
            key=re.findall(rex,line)
            # 如果找到合适的key
            if len(key) >0 :
                deletekey=key[0].split(",")[0]
                r.delete(deletekey)
            else:
                continue

if __name__ == "__main__":
    r1 = r"mid:.*?,"
    r2 = r"findByCiticOpenId:.*?,"
    r3=r"WX_ACTIVITY_USERINFO:.*?,"
    r4 = r"GET_WEIXIN_USER_INFO:.*?,"
    r5 = r"MEMBER_REDIS_CONFIG_PARAMETER_BASE:[0-9]{18}?,"
    filename = sys.argv[1]
    pool = redis.ConnectionPool(host='address', port=6379, db=0,password='password')
    r = redis.Redis(connection_pool=pool)
    findkey(r,r2)