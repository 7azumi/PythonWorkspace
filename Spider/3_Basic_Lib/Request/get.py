import requests

data = {
    'name': 'py',
    'age': 20
}
# -----GET-----
# url_1 = 'http://httpbin.org/get'
# r1 = requests.get(url_1,params=data)
# print(type(r1.text))
# print(r1.text)
# print(type(r1.json()))
# print(r1.json())


# headers = {
#     'User-Agent':'Chrome/66.0.3359.170'
# }
#
# url_2 = 'https://www.github.com/favicon.ico'
# r2 = requests.get(url_2,headers=headers)
# with open('github.ico','wb') as f:
#     f.write(r2.content)


# Cookies 登录
# headers = {
#     'User-Agent':'Chrome/66.0.3359.170',
#     'Cookie':'JSESSIONID=8C62D7548A5DD6F97BB4D452A43C8F58',
#
# }
# url_3 = 'http://jwgl.cqjtu.edu.cn/jsxsd/framework/xsMain.jsp'
# r3 = requests.get(url_3,headers=headers)
# print(r3.text)


# Session 模拟同一个会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/1234')
# r = s.get('http://httpbin.org/cookies',headers=headers)
# print(r.text)
url0 = 'https://www.casvot.com/?p=45'
url1 = 'https://www.12306.cn'
r = requests.get(url0, verify=False)
print(r.status_code)
print(r.headers)
