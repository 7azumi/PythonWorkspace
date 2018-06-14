import urllib.request
import requests

response = urllib.request.urlopen("http://www.baidu.com")
data = response.read()
print(type(response.getcode()))
