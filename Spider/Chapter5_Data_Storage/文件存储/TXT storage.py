import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/66.0.3359.170 Safari/537.36'
}

html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-feed.feed-item').items()

for item in items:
    question = item.find('h2').text()
    author = item.find('a.author-link').text()
    answer = pq(item.find('.content').html()).text()

    with open('explore.txt','a',encoding='utf-8') as file:
        file.write('\n'.join([question,author,answer]))
        file.write('\n' + '='*50 + '\n')