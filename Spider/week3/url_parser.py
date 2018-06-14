from bs4 import BeautifulSoup
import requests
import time,pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list1']
item_info = ceshi['item_info']

def get_links_from(channel,page,who_sell=0):
    # http://cq.58.com/shouji/pn3/
    list_view = '{}pn{}/'.format(channel,str(page))
    web_data = requests.get(list_view)
    soup = BeautifulSoup(web_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select("td.t  a.t"):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass


def get_info(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,"lxml")
    price = soup.select('span.price_now i')[0].text
    if price != '0':
        title = soup.title.text
        views = soup.select('.look_time')[0].text
        area  = list(soup.select('div.palce_li i')[0].text.split('-'))
        item_info.insert_one({'title':title,'url':url, 'price':price, 'views':views ,'area':area})
    else:pass


# get_links_from('http://cq.58.com/shouji/',2)

get_info('http://zhuanzhuan.58.com/detail/885421684606976006z.shtml')

# web_data = requests.get('http://zhuanzhuan.58.com/detail/985051695680906997003z.shtml')
