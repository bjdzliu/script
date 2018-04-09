# -*- coding: utf-8 -*-
import json
import urllib.parse
for line in open('1.log',encoding='gb18030'):
    column1 = line.split('.log:')[1]
    o = json.loads(column1)
    rawurl=o['legs'][1]['uri']
    url = urllib.parse.unquote(rawurl)
    print(url)



