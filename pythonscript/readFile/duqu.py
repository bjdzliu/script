import json
for line in open('ceshi'):
    # print line.split(',{')[0]
    # print '{'+ line.split(',{')[1]
    column1= line.split(',{')[0]
    column2 ='{'+ line.split(',{')[1]
    o = json.loads(column2)
    if 'GoogleMaps/RochesterNY' in o:
        print 'haha'
    print column1+ ':'+ o['a']
