import http.cookiejar
import urllib.request

# Cookies处理
cookie_file = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_file)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

for item in cookie:
    print(item.name+' = '+item.value)
