from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 如果是需要认证的代理，可设置成username:password@x.x.x.x:xx
proxy = '47.105.146.57:8118'
proxy_handler = ProxyHandler({
    'http':'http://' + proxy,
    'https': 'https://' + proxy,
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print("1" + e.reason)
