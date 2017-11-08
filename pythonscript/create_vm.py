#!/usr/bin/python
import urllib
import json
import time
import sys

vmnum=int(sys.argv[1])
def httppost(url,values,headers):
    params=json.dumps(values)
    req = urllib.Request(url, params, headers)
    response = urllib.urlopen(req)
    return response

def curl_keystone():
    url = 'http://129.40.179.170:5000/v3/auth/tokens'
    values={"auth":{"identity":{"methods":["password"],"password":{"user":{"name":"admin","domain":{"name":"default"},"password":"zlinux"}}}}}
    headers = {"Content-type":"application/json;utf-8","Accept":"application/json;utf-8"}
    unscopetoken=httppost(url,values,headers).headers['X-Subject-Token']
    '''
    Get scoped token
    '''
    values2={"auth":{"identity":{"methods":["token"],"token":{"id":unscopetoken}},"scope":{"project":{"id":"ae930c869bb741bebc50995d189ae37c"}}}}
    token=httppost(url,values2,headers).headers['X-Subject-Token']
    return token

def createvm():
    projectid='ae930c869bb741bebc50995d189ae37c'
    url2='http://129.40.179.170:8774/v2.1/'+projectid+'/servers'
    print(url2)
    tokenid=curl_keystone()
    headers = {"Content-type":"application/json;utf-8","Accept":"application/jsoni;utf-8","X-Auth-Token":tokenid}
    print(headers)
    for i in range(vmnum):
        vmjson={"server":{"block_device_mapping_v2":[{"boot_index":"0","uuid":"a8c676f6-d552-4f02-9128-226616285e57","volume_size":10,"source_type": "image","destination_type":"volume","delete_on_termination":True}],"flavorRef":"4d3ec866-d1f5-4867-ba6d-c46394343c87","name":"mytestp"+str(i),"networks":[{"uuid":"fccfe97d-8149-4818-9b7a-d2949e826f43"}]}}
        vmdata = json.dumps(vmjson)
        reqvm = urllib.Request(url2,vmdata,headers)
        print(vmdata)
        try:
          responsevm = urllib.urlopen(reqvm)
          code=responsevm.code
          print ("create success responsecode= %s" %(code))
        except urllib.error.HTTPError as e:
          print(e.code)
          print(e.read())
        time.sleep( 5 )
if __name__ == "__main__":
    createvm()
