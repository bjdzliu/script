# -*- coding: utf-8 -*-
"""
获取 key的种类和大小的对应关系

1 先在db中导出
.out a.txt
select key,sum(size_in_bytes) from memory group by key;
sed -i 's/:/|/' a.txt
sed -i 's/,/|/' a.txt
2 得到格式数据
GET_WEIXIN_USER_INFO|++wBsgDG+fGMCqrvSI00tulohOMZEzpGFvOQ/D1pM1sOmYQcknTilb/uuwkD7frp|520
3 分析第1列和第3列

4 重新统计，需要删除writefile
"""
import json

r=0
sum=0
dict2 = {}
with open("a.txt",'r') as f:
    for x in f:
        key=x.split('|')[0]
        bytes=x.split('|')[-1].replace("\n","")
        if key not in dict2:
            dict2[key] = int(float(bytes))
        else:
            dict2[key] += int(float(bytes))

with open('writefile', 'a') as f2:
    f2.write(json.dumps(dict2))


"""
查询key分类，及大小的和
writefile 是key和数量的关系字典

"""
sum2=0
with open("writefile","r") as f:
     for x in f:
         dict1=json.loads(x)
         for k,v in dict1.items():
             if v/1024/1024 > 5:
                 sum2+=v/1024/1024
                 print "exceed 5m key sum is", k
print sum2