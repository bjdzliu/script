import json
import urllib
import urllib.request
import re
from operator import itemgetter, attrgetter

url="http://9.181.159.230:37125/v2/ubuntu/tags/list"
itdiffer = urllib.request.urlopen(url)
data=itdiffer.read()
listtag=json.loads(data)['tags']
print(listtag)
listtag2=[]
for x in listtag:
    listtag2.append(tuple(re.split(r'-',x)))
latesttag=sorted(listtag2,reverse = True)[0]
print('latest tag in registry is:','-'.join(list(tuple(latesttag))))

#print(test)
list2=['10-16-16-32', '10-16-17-32', '11-12-17-32', '16-12-17-32','16-13-17-32','16-13-18-32']
list3=[]
for x in list2:
    print(x)
    list3.append(tuple(re.split(r'-',x)))
print('list3 is',list3)
latest=sorted(list3,reverse = True)[0]
print('latest is',list(tuple(latest)))
print('-'.join(list(tuple(latest))))
#print(sorted(list3,reverse = True)[0])
