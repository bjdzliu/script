import os
import re

#find redis conf in many projects

def readlist(listfile):
    with open(listfile,'r') as f:
       for line in f.readlines():
          print(line.strip())
          findindir(line.strip())


def findindir(linedir):
    my_redishost=re.compile(r".*redis.rds.aliyuncs.com")
    for dirpath, dirnames, filenames in os.walk(linedir):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if my_pl.findall(fullpath):
              with open(fullpath,'r') as f2:
                for line in f2.readlines():
                   if my_redishost.findall(line):
                      print fullpath+" "+line

if __name__ == "__main__":
    global my_pl
    listfile="./lm_prod"
    listfile="./lm_prod"
    my_pl = re.compile(r".*prod.yml|.*prod.properties")

    readlist(listfile)
