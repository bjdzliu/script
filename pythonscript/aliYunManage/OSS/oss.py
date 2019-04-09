# -*- coding: utf-8 -*-
# 以下代码实现文件的备份，删除和上传。
# Endpoint可以是：
#   http://oss-cn-hangzhou.aliyuncs.com
#   https://oss-cn-hangzhou.aliyuncs.com
# 分别以HTTP、HTTPS协议访问。
import os
import shutil

import oss2,datetime,Queue
import threading



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

    def put_file_name(self,file_dir):
        for root, dirs, files in os.walk(file_dir, topdown=True):
            # print(root,dirs,files) #当前目录路径
            if files:
                for files1 in files:
                    localdir = os.path.join(root, files1)
                    print(localdir)
                    self.bucket.put_object_from_file(localdir, localdir)

    def delete_file(self,file):
        if isinstance(file, list):
            self.bucket.batch_delete_objects(file)
        else:
            self.bucket.delete_object(file)

### src is either a list or a file,such as:
### src = self.genfilelist()
### src = file
### despath = 'lm-web/temp/'

    def runthread(self,q,timestamp):
        while True:
            if q.qsize() > 0:
                listkey=q.get()
                files = listkey.split('/', 1)[1]
                self.bucket.copy_object(self.bucket_name, listkey, despath + timestamp + '/' + files)
            else:
                break

    def copyfile(self,despath,src):
        q = Queue.Queue()
        threads = []
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y%m%d%H%M')
        if isinstance(src, list):

            print("Start to copy src files to " + despath + timestamp)
            for listkey in src:
               q.put(listkey)

            for i in range(5):
                t = threading.Thread(target=self.runthread,args=(q,timestamp,))
                threads.append(t)
            #start run thread
            for i in range(5):
                threads[i].start()

            print("END copy src files to " + despath + timestamp)

             # print("start to copy src files to " + despath + timestamp)
             # for listkey in src:
             #    files = listkey.split('/', 1)[1]
             #    self.bucket.copy_object(self.bucket_name, listkey, despath + timestamp + '/' + files)
             # print(" END copy src files to " + despath + timestamp)
        else:
            # copy index.html
            print("start to copy " + src + " to "+ despath+timestamp)
            self.bucket.copy_object(self.bucket_name, src, despath + timestamp + '/' + src)

if __name__ == '__main__':
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'xxxxx')
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'xxxxx')
    bucket_name = os.getenv('OSS_TEST_BUCKET', 'xxxxx')
    endpoint = os.getenv('OSS_TEST_ENDPOINT', 'https://oss-cn-beijing.aliyuncs.com')
    BFManager = BucketFileManage(access_key_id,access_key_secret,bucket_name,endpoint)
    #staticfiledir is the substr of bucket/lm-web/static
    staticfiledir = 'lm-web/static'
    srclist=BFManager.genfilelist(staticfiledir)
    srcfile='lm-web/index.html'
    despath='lm-web/temp/'
    BFManager.copyfile(despath,srclist)
    BFManager.copyfile(despath,srcfile)
    #BFManager.delete_file(srclist)
    #BFManager.delete_file(srcfile)
    #BFManager.put_file_name('lm-web')


### upload files
#bucket.put_object_from_file('remote.txt', 'local.txt')



