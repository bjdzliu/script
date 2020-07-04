import requests
res = requests.get('https://xxxxxx.cs-cn-beijing.aliyun.com:20154/projects/', verify='./cert/ca.pem', cert=('./cert/cert.pem', './cert/key.pem'))
requests.post()

print res.content