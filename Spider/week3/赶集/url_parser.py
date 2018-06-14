from bs4 import BeautifulSoup
import requests,random,pymongo

headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) \
    AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
item_list = ganji['item_list']
item_info = ganji['item_info']


# spider 1
def get_pages_item_links(url,page):
    page_url = '{}o{}/'.format(url,page)
    web_data = requests.get(page_url,headers=headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    if soup.find('a','linkOn'):
        for link in soup.select('td.t a'):
            item_link = link.get('href')
            if 'htm' not in item_link.split('.'):
                item_list.insert_one({'item_url':item_link.split('?')[0]})
    else:pass

# get_pages_item_links('http://bj.ganji.com/jiaju/',3)

# spider 2
def get_info(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,"lxml")
    price = soup.select('span.price_now i')[0].text
    if price != '0':
        title = soup.select('.info_titile')[0].text
        area  = list(soup.select('div.palce_li i')[0].text.split('-'))
        item_info.insert_one({'title':title,'url':url, 'price':price,'area':area})
    else:pass

# get_info('http://zhuanzhuan.ganji.com/detail/990472299295801345z.shtml')