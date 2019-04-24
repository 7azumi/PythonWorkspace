#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.baidu.com"
# "https://www.liuxue86.com/a/3713634.html"
r = requests.get(url)
print(r.encoding)
# r.encoding = "utf-8"
print(r.text)
# print(data.headers)

# soup = BeautifulSoup(data.text, 'lxml')
# print(type(soup))
# print(soup.decode("utf-8"))