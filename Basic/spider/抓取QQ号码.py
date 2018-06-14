import urllib.request
import re
import ssl


def writeHtmlByte(htmlbytes,toPath):
    with open(toPath, 'wb') as f:
        f.write(htmlbytes)
def writeHtmlStr(htmlbytes,toPath):
    with open(toPath, 'w') as f:
        f.write(htmlbytes.decode('utf-8'))


def getResponse(url):
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url,context=context)
    return response.read()


def qqSpider(url, toPath=''):
    res = getResponse(url)

    html = str(res)
    pat = r"[1-9]\d{4,9}"
    reQQ = re.compile(pat)

    qqslist = reQQ.findall(html)
    qqslist = list(set(qqslist))
    print(qqslist)
    print(len(qqslist))




url = 'https://www.douban.com/group/topic/80013363/'
qqSpider(url)