# -*- coding: utf-8 -*-
"""
计算key的种类和数量的对应关系
0,string,u:p:18786420939,416,string,255,255,2019-08-13T13:50:40.024000

"""
import sys,json
reload(sys)
sys.setdefaultencoding('utf-8')

# with open("analyse","r") as file:
#     for line in file:
#         newcontent=line.split(",",4)[2]
#         print(newcontent)
#         newcontent2=newcontent.split(":",1)
#         print(newcontent2)

import csv
# r 人工读写的  rb 适用于非人工读写的
with open('analyse','rb') as csvfile:
 print  type(line.replace('\0', '') for line in csvfile)
 reader = csv.DictReader(csvfile)
 dict2={}
 for row in reader:
    key=row["key"].split(":", 1)[0]
    if  key not in dict2:
        dict2[key]=1
    else:
        dict2[key]+=1
#print dict2
with open('analyse.out', 'a') as f:
    f.write(json.dumps(dict2))

