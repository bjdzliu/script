# -*- coding: utf-8 -*-
import json,csv
import yaml
import http.client
import mimetypes
from urllib import request
import urllib.parse

"""
#generate a file named zonelist
dns.py -g zonelist 

# AZ CLI
az network private-dns record-set list -g rg-dp-privatezone-shs-tuidemo -z tui.shs.dp.internal.vgcserv.com.cn

# Generate a record list for every zone list
dns.py -f zonelist -o recordlist

# recordlist.csv include 
Name , Type, Value, Zonename

"""

# 获取yaml文件路径
def ReadConf():
    yamlPath='credential'
    with open(yamlPath,'rb') as f:
        # salf_load_all方法得到的是一个迭代器，需要使用list()方法转换为列表
        # safe_load return 
        data = yaml.safe_load(f)
        dict1={}
        dict1['client_id'] = data['credential']['sp-tuidemo-client-id']
        dict1['subscription_id'] = data['credential']['sp-tuidemo-subscription-id']
        dict1['tenant_id'] = data['credential']['sp-tuidemo-tenant-id']
        dict1['client_secret'] = data['credential']['sp-tuidemo-client-secret']
    return dict1

# 获取Token
def GetToken(confkv):

    conn = http.client.HTTPSConnection("login.chinacloudapi.cn")
    
    tenant_id=confkv['tenant_id']
    subscription_id=confkv['subscription_id']
    client_id=confkv['client_id']
    client_secret=confkv['client_secret']

    URI='%s%s%s' % ('/', tenant_id, '/oauth2/token')
    
    s1='grant_type=client_credentials'
    s2='client_id='+client_id
    s3='client_secret='+client_secret
    s4='resource=https://management.chinacloudapi.cn'
    payload= f'{s1}&{s2}&{s3}&{s4}'

    
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("GET", URI, payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    #print(data.decode("utf-8"))
    token_in_str=json.loads(data)['access_token']
    return token_in_str


# 获取zone list
def GetZoneList(token,confkv):
    #GET https://management.azure.com/subscriptions/subid/providers/Microsoft.Network/dnszones?api-version=2018-05-01

    conn = http.client.HTTPSConnection("management.chinacloudapi.cn")

    subscription_id=confkv['subscription_id']

    payload = ''
    BearerToken = '%s %s' % ('Bearer', token)
    headers = {
    'Authorization': BearerToken
    }

    s1=subscription_id

    URI="/subscriptions/"+s1+"/providers/Microsoft.Network/privateDnsZones?api-version=2018-09-01"

    conn.request("GET", URI, payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data


# 请求DNS record 资源
def QueryRecords(token,zonedict):
    #GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/recordsets?api-version=2018-05-01
    BearerToken = '%s %s' % ('Bearer', token)
    headers = {
    'Authorization': BearerToken
    }
    # 依次遍历zone name
    for zoneItem,zoneId in zonedict.items():

        params = urllib.parse.urlencode({'api-version': '2018-09-01'})
        main_domain= "https://management.chinacloudapi.cn"
        URI=zoneId+"/recordsets?%s" % params
        #if use “data” in Request, it's POST
        url=main_domain+URI
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req)
        #返回字节流，用decode编码
        recordsStr=res.read().decode("utf-8")
        recordsDict=json.loads(recordsStr)
        recordsList=recordsDict["value"]
        #建一个list，保存每次遍历的record list,每个zone name遍历后，一次写入csv文件
        writeToCsvList=[]
        print("##### Zone name >>>>>",zoneItem)
        # 依次遍历每个zone name中的多个记录，从record中挑选有用的值，放到record_4_elements list中，然后写入csv文件
        for single_record in recordsList:

            record_4_elements=[zoneItem]
            record_4_elements.append(single_record['name'])
            record_4_elements.append(single_record['type'])
            
            #print("A Record is: ",single_record['properties'])
            for k,v in single_record['properties'].items():
                if k=="aRecords":
                    record_4_elements.append(v)
            writeToCsvList.append(record_4_elements)
        
        
        with open('./records_output.csv', 'a+',newline='\n') as csv_file:
            for itemInCsv in writeToCsvList:
                writer = csv.writer(csv_file,dialect='excel-tab')
                '''
                dialect : default is excel
                excel-tab is build in . 
                '''
                writer.writerow(itemInCsv)                   
    

if __name__ == '__main__':
    #获取密钥信息，required
    confkv=ReadConf()
    #获取请求token，required
    token=GetToken(confkv)
    #获取资源信息，required
    zoneName=GetZoneList(token,confkv)
    zoneDict=json.loads(zoneName)
    # key's name is "value", the value content is all zone name"

    for k,v in zoneDict.items():
        zonelist=[]
        zonedict={}
        for listItem in v:
            #保存一份zone list
            zonelist.append(listItem['name'])
            #保存 一个dict，zone name和zone id的对应，以便获取records
            zonedict[listItem['name']]=listItem['id']
            print(listItem['name'],listItem['properties']['numberOfRecordSets'])
            
    
    # 获取zone里面的records
    QueryRecords(token,zonedict)



