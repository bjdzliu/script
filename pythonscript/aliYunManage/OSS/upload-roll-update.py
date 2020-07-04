# -*- coding: utf-8 -*-
####################################
#Provided for lianmeng test env deployment
#author liudz@citic.com
####################################
"""
每次build出来的static file 都方在一个日期目录里
nginx中的root dir配置成这个新的目录
避免用户微信端访问新版时可能出现的白屏问题
"""
import os
import shutil
import sys

import oss2,datetime


newstaticpath = sys.argv[1]
class BucketFileManage(object):
    def __init__(self,access_key_id,access_key_secret,bucket_name,endpoint):
        self.access_key_id=access_key_id
        self.access_key_secret=access_key_secret
        self.bucket_name=bucket_name
        self.endpoint=endpoint
        # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
        self.bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint, self.bucket_name)
    def list(self,path):
        for obj in oss2.ObjectIterator(self.bucket, delimiter=path):
            if obj.is_prefix():  # 文件夹
                print('directory: ' + obj.key)
            else:  # 文件
                print('file: ' + obj.key)

    def genfilelist(self,staticfiledir):
        myownlist = []
        for b in oss2.ObjectIterator(self.bucket, prefix=staticfiledir, max_keys=500):
            myownlist.append(b.key)
        return myownlist

    def put_file_name(self,remote_dir,local_dir):
        for root, dirs, files in os.walk(local_dir, topdown=True):
            print("dangqian mulu lu jing",root,dirs,files) #当前目录路径
            #('dangqian mulu lu jing', 'lm-wheel/js', [], ['app.ca1d992c75284b1fc62e.js', 'manifest.31d376c580e825222896.js', 'vendor.c7f21f08684452949e09.js'])
            if files:
                for files1 in files:
                    localfile = os.path.join(root, files1)
                    #print(localfile)
                    #remote_dir is key in oss
                    self.bucket.put_object_from_file(remote_dir+localfile, localfile)
    def delete_file(self,file):
        if isinstance(file, list):
            self.bucket.batch_delete_objects(file)
        else:
            self.bucket.delete_object(file)

### src is either a list or a file,such as:
### src = self.genfilelist()
### src = file
### despath = 'lm-web/temp/'

    def copyfile(self,despath,src):
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y%m%d%H%M')
        if isinstance(src, list):
	     print("start to copy src files to " + despath + timestamp)
             for listkey in src:
                files = listkey.split('/', 1)[1]
                self.bucket.copy_object(self.bucket_name, listkey, despath + timestamp + '/' + files)
             print(" END copy src files to " + despath + timestamp)
        else:
            # copy index.html
            print("start to copy " + src + " to "+ despath+timestamp)
            self.bucket.copy_object(self.bucket_name, src, despath + timestamp + '/' + src)

if __name__ == '__main__':
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'xxxxx')
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'xxxxx')
    bucket_name = os.getenv('OSS_TEST_BUCKET', 'lm-citic')
    endpoint = os.getenv('OSS_TEST_ENDPOINT', 'https://oss-cn-beijing.aliyuncs.com')
    BFManager = BucketFileManage(access_key_id,access_key_secret,bucket_name,endpoint)

 ### ready to backup file and dir in oss 
    backuplist=['lm-activity/lm-wheel/img','lm-activity/lm-wheel/css','lm-activity/lm-wheel/js','lm-activity/lm-wheel/static']
    singlefile=['lm-activity/lm-wheel/index.html']
    despath='lm-activity/lm-wheel/temp/'

###### no need to backup
#    for i in backuplist:
#        srclist=BFManager.genfilelist(i)
#        BFManager.copyfile(despath,srclist)
#        BFManager.delete_file(srclist)
#    BFManager.copyfile(despath,singlefile[0])
#   BFManager.delete_file(singlefile[0])
### end backup

    BFManager.put_file_name('lm-web/roll_update/',newstaticpath)

