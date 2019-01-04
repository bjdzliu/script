# -*- coding: utf-8 -*-
#content of 1.log is like group-3_instance-4_2018-03-15-22-09.log:{"type":"transaction", "time":1521122825922, "path":"/citiccloud/alisms/v1/SendSms", "protocol":"https", "protocolSrc":"8065", "duration":26, "status":"success", "serviceContexts":[{"service":"aliSMS", "monitor":true, "client":"aedf0d2b-29e4-4c8b-ad88-903da2bed557", "org":"ORG中信重工远程诊断", "app":"APP中信重工远程诊断", "method":"SendSms", "status":"success", "duration":6}], "customMsgAtts":{}, "correlationId":"097eaa5a9099a9e633064e22", "legs":[{"uri":"/citiccloud/alisms/v1/SendSms", "status":500, "statustext":"Internal Server Error", "method":"GET", "vhost":null, "wafStatus":0, "bytesSent":0, "bytesReceived":0, "remoteName":"10.76.2.17", "remoteAddr":"10.76.2.17", "localAddr":"10.247.32.78", "remotePort":"49409", "localPort":"8065", "sslsubject":null, "leg":0, "timestamp":1521122825895, "duration":27, "serviceName":"aliSMS", "subject":"aedf0d2b-29e4-4c8b-ad88-903da2bed557", "operation":"SendSms", "type":"http", "finalStatus":"Pass"}, {"uri":"/citiccloud/alisms/v1/SendSms?OwnerId=1611274168981246&PhoneNumbers=17600717588&SignName=%E4%B8%AD%E4%BF%A1%E9%87%8D%E5%B7%A5&TemplateCode=SMS_103510043&TemplateParam=%7B%5C%22name1%5C%22%3A%5C%22%E5%B8%B8%E8%89%B3%E5%85%B5%5C%22%2C%5C%22name2%5C%22%3A%5C%22%E8%B1%AB%E5%85%89%E9%87%91%E9%93%85%E7%8E%89%E5%B7%9D%E5%8D%8A%E8%87%AA%E7%A3%A8%5C%22%2C%5C%22name3%5C%22%3A%5C%22%E6%95%85%E9%9A%9C%5C%22%2C%5C%22code%5C%22%3A%5C%22%E6%85%A2%E9%A9%B1%E4%BE%A7%E5%9B%BA%E5%AE%9A%E7%AB%AF%E8%BD%B4%E6%89%BF%E6%B8%A9%E5%BA%A6%E5%80%BC%E7%9B%91%E6%8E%A7+++%E5%8F%91%E9%80%81%E6%97%B6%E9%97%B4%3A2018-03-15+22%3A07%3A05%5C%22%7D", "status":500, "statustext":"Internal Server Error", "method":"GET", "vhost":null, "wafStatus":0, "bytesSent":0, "bytesReceived":0, "remoteName":"localhost", "remoteAddr":"127.0.0.1", "localAddr":"127.0.0.1", "remotePort":"8080", "localPort":"45150", "sslsubject":null, "leg":1, "timestamp":1521122825920, "duration":2, "serviceName":"aliSMS", "subject":"aedf0d2b-29e4-4c8b-ad88-903da2bed557", "operation":"SendSms", "type":"http", "finalStatus":null}]}
import json
import urllib.parse
for line in open('1.log',encoding='gb18030'):
    column1 = line.split('.log:')[1]
    o = json.loads(column1)
    rawurl=o['legs'][1]['uri']
    url = urllib.parse.unquote(rawurl)
    print(url)



