from lxml import etree

data = etree.parse('./test1.html', etree.HTMLParser())
result = data.xpath('//ul//@href')
print(result)
print(result[0])

