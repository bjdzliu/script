import subprocess,sys,os,re
"""
exec : . set_swarm_env.sh ; python collect.py {appname}

"""
container=[]
copymap={}

cmd ="docker ps |grep " + sys.argv[1] + " |awk '{print $1}'"
p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
p.wait()
#print p.stdout.read()
for line in p.stdout.readlines():
  container.append(line.replace("\n",""))

for id in container:
  cmd="docker inspect --format '{{.NetworkSettings.Ports}}%{{.LogPath}}' "+id
  output = os.popen(cmd)
  str = output.read().replace("\n","")
  hostip = re.findall(r'(?:\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)',str)[0]
  addr = re.findall(r'%.+',str)
  logaddr = addr[0].strip('%')
#  print addr[0].strip('%')
  copymap[logaddr] = hostip

for k,v in copymap.items():
  print k,v
  cmd = "scp " + v + ":" + k + " /root/liudz/collectlog"
  print cmd
  #returncode = subprocess.call(cmd)
  p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
  p.wait()
