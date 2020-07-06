# -*- coding: utf-8 -*-
import json,csv

"""
az postgres server list> server_list.json
sample data is like
[
  {
    "administratorLogin": "psqladmin",
    "byokEnforcement": "Disabled",
    "sku": {
      "capacity": 2,
    },
    "sslEnforcement": "Enabled",
    "storageProfile": {
      "storageMb": 5120
    }
    }
]
    
"""
filename = ('./server_list.json')

'''
jsObj is a list, the elements is dict type in this list
'''
jsObj = json.load(open(filename))


'''
first need clear previous file output
clear content in output.csv
'''

with open('./servers_output.csv', 'a+') as f:
    f.seek(0)
    f.truncate()


for i in jsObj:
    storage=int(i["storageProfile"]["storageMb"]/1024)
    server_name=i["name"]
    rg=i["resourceGroup"]
    vcores=i["sku"]['capacity']

    #str1 = f'{server_name} , {rg} , {vcores} ,{storage}'

    str1 = f'az postgres db list -g {rg} -s {server_name}  && ^'
    with open('./az_list_db.bat', 'a+') as batfile:
        batfile.write(str1+"\n")
    '''
    in windows10 cmd execute 
    az login
    ./az_list_db.bat and we get db list in dblist file
    '''
    print("")
    '''
    如果使用str1作为参数write.writerow(str1) ,output 如下：
    p,g,q,l,-,d,p,-,c,o,n,......
    '''
    list1=[server_name,rg,vcores,storage]
    # use newline='' to delete space line between real data
    with open('./servers_output.csv', 'a+',newline='') as csv_file:
        writer = csv.writer(csv_file,dialect='excel-tab')
        '''
        dialect : default is excel
        excel-tab is build in . 
        '''
        writer.writerow(list1)

   # print(server_dict[])
