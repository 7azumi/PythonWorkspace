import urllib.request
import random

userAgent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) \
    AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) \
    AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
]
url = "http://www.baidu.com"

headerStr = random.choice(userAgent)
req = urllib.request.Request(url)
req.add_header("User-Agent",headerStr)

response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
