import json
#list to str
l=['a','b','c']
str1=''.join(l)
print(str1)

#convert value to str in list
l2=['a',1,3,4,'b','c']
newl2=[str(i) for i in l2]
print(newl2)

## str to list
str2='abcde'
newlist2=list(str2)
print(newlist2)
###
str2='a,b,c,d,e'
newlist3=str2.split(',')
print(newlist3)

## list to dict
ldict=['a','b','c']
t=[2,3,4]
newdict=dict(zip(l,t))
print(newdict)


ldict2=[['1',2],['a',4]]
print(dict(ldict2))

### dict to list
d={'a':1,'b':2}
print("dict keys in list : %s" % list(d.keys()) )
print("dict values in list : %s" % list(d.values()) )

#### str to dict
str3="{'at':1,'bt':2}"
out=eval(str3)
print(out)


str3='{"at":1,"bt":2}'
out2=json.loads(str3)
print(out2)

#### dict to str
str5=json.dumps(out2)
print('dict to str is:  %s  '% str5)

