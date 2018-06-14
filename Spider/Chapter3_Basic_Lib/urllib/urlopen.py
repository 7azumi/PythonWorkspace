from urllib import request

url = 'https://www.casvot.com'
url1 = 'http://www.12306.cn'
# urlopen
# res = urllib.request.urlopen(url)
# print(res.getheader('Server'))

# request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/66.0.3359.170 Safari/537.36'
}
req = request.Request(url=url1, headers=headers)
res = request.urlopen(req, timeout=1)
print(res.status)
print(res.getheaders())
