'''登录成功	http://124.221.164.9:39002/manager/user/login		post	json	"{
 "phone": "15100000000",
 "password": "123520ABc"
}"
'''
#1、导入包
import requests
class TestApi:
	token = requests.session() #定义一个全局类变量
#2、定义登录方法

#登录用户
	def test_login(self):
	#3、定义测试数据
		url = 'http://124.221.164.9:39002/manager/user/login'
		datas = {
			 "phone": "admin",
			 "password": "123456"
			}
	#4、使用requests.token全局类变量发送请求
		res = TestApi.token.request(method='post',url=url,data=datas,headers={"Content-Type":"application/json")
		print(res.json())


#新增用户
	def test_useradd(self):
	#定义测试数据
		url='http://124.221.164.9:39002/manager/user'
		data={
			"id": 0,
			"phone": "15181199999",
			"userName": "tiantian1",
			"deptId": 1,
			"deptName": "",
			"rankType": 1,
			"rankName": "",
			"roles": [],
			"postName": "",
			"profilePicture": "",
			"fingerPath": "",
			"localFinger": "",
			"email": "",
			"routers": [
				{
					"path": "",
					"name": "",
					"redirect": "",
					"component": "",
					"meta": {
						"title": "",
						"icon": ""
					},
					"children": [
						{}
					]
				}
			],
			"menuList": [
				{
					"path": "",
					"name": "",
					"redirect": "",
					"component": "",
					"meta": {
						"title": "",
						"icon": ""
					},
					"children": [
						{}
					]
				}
			],
			"createTime": "",
			"createBy": "",
			"updateTime": "",
			"updateBy": ""
		}
		res = TestApi.token.request(method='post',url=url,params=data)
		print(res.json())

#获取用户
	def test_user_byToken(self):
		url = 'http://124.221.164.9:39002/manager/user/user/byToken'
		res = TestApi.token.request(method='get',url=url,params=None)
		print(res.json())

	def test_userDelete(self):
		url='http://124.221.164.9:39002/manager/user/{0}'
		res= TestApi.token.request(method='DELETE',url=url)
		print(res.json())



if __name__=='__main__':
    TestApi.test_login()
	#TestApi.test_useradd()
	#TestApi.test_user_byToken()
	#TestApi.test_userDelete()

