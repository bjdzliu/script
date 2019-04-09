# -*- coding: utf-8 -*-

import sys,getopt
import gitlab
gl = gitlab.Gitlab('https://gitlabaddress', private_token='xxxxxx',api_version='3')


try:
    options,args = getopt.getopt(sys.argv[1:],"hp:d:",["merge","newrelease","src=","dst=","repo="])
except getopt.GetoptError:
    sys.exit()

# collect parameters and convert to a dict
def getValue(options):
    list1=[]
    dict1={}
    for name,value in options:
        if name in ("-d","--dst"):
            print 'destination branch is ',value
            dict1['dst']=value
        if name in ("-s","--src"):
            print 'source branchis----',value
            dict1['src'] = value
        if name in ("-r","--repo"):
            print 'repo is----',value
            repolist=value.split(",")
            for single_repo in repolist:
                dict1['repo'] = single_repo
                dictnew=dict1.copy()
                list1.append(dictnew)

    return list1

# Create release branch
def generateRelease(dict1):
    repo=dict1['repo']
    destbranch=dict1['dst']
    srcbranch=dict1['src']
    project = gl.projects.get(repo)
# destbranch is a new release
    result = project.branches.create({'branch_name': destbranch,'ref': srcbranch})
    return result

# Merge branch
def merge(dict1):
    repo = dict1['repo']
    destbranch=dict1['dst']
    srcbranch=dict1['src']
    project = gl.projects.get(repo)
    mr = project.mergerequests.create({'source_branch': srcbranch,
                                       'target_branch': destbranch,
                                       'title': 'merge from'+destbranch
                                       })
    try:
      result=mr.merge()
      print result
    except:
      print "error,check gitaddress website"

# Delete branch
# def delete(dict1):
#     dict1
#     project.branches.delete('feature1')

print getValue(options)

myParametersDictList=getValue(options)



#options is list type,contain tuple
if ('--merge', '') in set(options):
    for singleDict in myParametersDictList:
        print singleDict
        merge(singleDict)
    pass
elif ('--newrelease', '') in set(options):
    for singleDict in myParametersDictList:
        print singleDict
        generateRelease(singleDict)
    pass
else:
    pass

