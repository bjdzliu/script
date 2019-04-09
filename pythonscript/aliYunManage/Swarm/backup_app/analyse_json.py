#!/usr/bin/env Python
# coding=utf-8

import os,json

"""
appservices.json is a json format file

"""

exclude_list=['acslogging','acsmonitoring','acsvolumedriver','acsrouting']

def analyse():
    with open('./appservices.json','r') as file:
        output=json.load(file)
        for i in output:
            #print  unicode(i, encoding='utf-8')
            if i['name'] not in exclude_list:
              write=open('./appyaml/'+i['name'],'w')
              write.write(i['template'])
              write.close()

def clearBlankLine():
    pass


if __name__ == "__main__":
    analyse()