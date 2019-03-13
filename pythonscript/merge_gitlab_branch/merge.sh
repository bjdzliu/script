#!/bin/bash
#put in jenkins
result=$(echo "$dest_branch" | grep "release/")
if [[ "$result" != "" ]]
then
   # "contain release and will createe release/xxxxx"
 python  merge_branch.py --newrelease --src=$source_branch --dst=$dest_branch --repo=$listrepo

else
 python  merge_branch.py --merge --src=$source_branch --dst=$dest_branch --repo=$listrepo
fi