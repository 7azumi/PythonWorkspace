from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


br = webdriver.Chrome()

br.get('https://www.zhihu.com/explore')
print(br.get_cookies())
br.add_cookie({'name': 'JSESSIONID', 'domin': 'jwgl.cqjtu.edu.cn', 'value': 'B4B677C63C2313CF0CE54BE254A79E42'})
print(br.get_cookies())
