#1、导入requests包
import requests
#2、发送get请求
res=requests.get('http://124.221.164.9:39002/manager/user/user/byToken')
#3、打印结果
print(res.json())