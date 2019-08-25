# -*- coding: utf-8 -*-
"""
python3
"""
import csv,sys,time
# 元组
DATA=(
    (u'学科编号',u'学科',u'人数'),
    (u'1', u'java', u'2'),
    (u'2', u'php', u'33'),
    (u'3', u'python', u'44'),
)

start = time.clock()
print ('*** save csv')

f=open('xuexi.csv','w',newline='',encoding='utf-8-sig')

# f.write("aaaaaa")
# sys.exit(0)
# csv文件的写入
# writer 可迭代对象
writer = csv.writer(f)

for record in DATA:
    writer.writerow(record)
f.close()

## 读取csv文件
f=open("xuexi.csv",'r',newline='',encoding='utf-8-sig')
reader=csv.reader(f)
for no,name,num in reader:
    print('%s,%s,%s'%(no,name,num))
f.close()

"""
csv.DictReader类和csv.DictWriter 将csv写入字典
"""

with open("xuexi.csv",encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #循环打印数据的id和class值，此循环执行7次
        print(row[u'学科编号'],row[u'学科'],row[u'人数'])


end = time.clock()
print(end-start)