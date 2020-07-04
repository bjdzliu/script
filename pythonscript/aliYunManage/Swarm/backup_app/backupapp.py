#!/usr/bin/env Python
# coding=utf-8
"""
curl -s -v -X GET -k --cert ../cert/cert.pem --key ../cert/key.pem https://xxxxxxxx.cs-cn-beijing.aliyun.com:20080/projects/

create app from backyaml file in this script

"""

import json,httplib
import socket,ssl

exclude_list=['acslogging','acsmonitoring','acsvolumedriver','acsrouting']

class HTTPSClientAuthConnection(httplib.HTTPSConnection):
    def __init__(self, host, port, key_file, cert_file, ca_file, timeout=None):
        httplib.HTTPSConnection.__init__(self, host, key_file=key_file, cert_file=cert_file)
        self.key_file = key_file
        self.cert_file = cert_file
        self.ca_file = ca_file
        self.timeout = timeout
        self.host=host
        self.port=port

    def connect(self):
        sock = socket.create_connection(address=(self.host, self.port), timeout=self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        #If there's no CA File, don't force Server Certificate Check
        if self.ca_file:
            self.sock = ssl.wrap_socket(sock, keyfile=self.key_file, certfile=self.cert_file, ca_certs=self.ca_file, cert_reqs=ssl.CERT_REQUIRED)
        else:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, cert_reqs=ssl.CERT_NONE)


#indenpent connect and save yaml
def getjson():
     conn = httplib.HTTPSConnection(host="xxxxxxx.cs-cn-beijing.aliyun.com",key_file="./cert/key.pem",cert_file="./cert/cert.pem")
     initsocket= socket.create_connection(address=("xxxxxxx.cs-cn-beijing.aliyun.com",20080))
     try:
         conn.sock=ssl.wrap_socket(initsocket,ca_certs="./cert/ca.pem",certfile="./cert/cert.pem",keyfile="./cert/key.pem",cert_reqs=ssl.CERT_REQUIRED)
     except ssl.SSLError,e:
         print e
     conn.request("GET", "/projects/")
     r1 = conn.getresponse()
     print r1.status,r1.reason
     savelocal=open("./testyaml.bak2","w")
     savelocal.write(r1.read())
     savelocal.close()


def analyse():
    file = open('./prodyaml.bak', 'r')
    line = file.readline()
    namelist = json.loads(line)
    for name in namelist:
         filename = './appyaml/' + name['name']
         # filename  was automatily formatted in linux
         if name['name'] not in exclude_list:
             writefobj = open(filename, 'w')
             writefobj.write(name['template'])
             writefobj.close()
    file.close()


def clearBlankLine(file2,file3):
    file1=open(file2, 'r')
    file2=open(file3, 'w')
    try:
        for line in file1.readlines():
            if line == '\n':   # replace to '\r\n' in windows
                print "n",line
                line = line.strip("")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


"""
create app from a testyaml.bak that get from /projects
"""
def cereate():
    header={"Content-Type": "application/json"}
    yamlopen=open("./testyaml.bak","r")
    for line in yamlopen:
        namelist = json.loads(line)
        for name in namelist:
            #if name['name'] == "nginx-delete":
            appname=name['name']
            apptemplate=name['template']
            d = dict(name=appname, template=apptemplate)
            d1=json.dumps(d)
            conn.request("POST","/projects/",d1,header)
    yamlopen.close()

def backup():
    pass

def listfile(file_dir):
        for root, dirs, files in os.walk(file_dir, topdown=True):
            # print(root,dirs,files) #当前目录路径
            if files:
                for files1 in files:
                    localdir = os.path.join(root, files1)
                    print(localdir)

if __name__ == "__main__":
    key_file="./cert/key.pem"
    cert_file="./cert/cert.pem"
    ca_file="./cert/ca.pem"
    host="xxxxxxxx.cs-cn-beijing.aliyun.com"
    port=20080
    timeout=5.0
    conn=HTTPSClientAuthConnection(host,port,key_file,cert_file, ca_file, timeout)

    ##get yaml
    conn.request("GET", "/projects/")
    r1 = conn.getresponse()
    print r1.status,r1.reason
    savelocal=open("./prodyaml.bak","w")
    savelocal.write(r1.read())
    savelocal.close()

    analyse()

    #clearBlankLine("./appyaml/citic-activity-bespeak","./appyaml/citic-activity-bespeak.yaml")
