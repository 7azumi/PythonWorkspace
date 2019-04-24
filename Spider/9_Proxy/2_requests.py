import requests

# 如果是需要认证的代理，可设置成username:password@x.x.x.x:xx
proxy = '47.105.146.57:8118'
proxies = {
    'http':'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error", e.args)
