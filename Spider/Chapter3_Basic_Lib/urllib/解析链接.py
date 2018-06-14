from urllib.parse import urlparse, unquote

result = urlparse('www.baidu.com/s?tn=baidu&wd=python&rsv_crq=6&bs=python')
# print(type(result),result)

url = 'www.baidu.com?kw=%E7%BC%B4%E8%B4%B9%E5%8D%95'
print(unquote(url))