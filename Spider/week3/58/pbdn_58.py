from bs4 import BeautifulSoup
import requests
import pymongo



client = pymongo.MongoClient('localhost',27017)
ceshi2 = client['ceshi2']
item_links = ceshi2['item_links']
item_info = ceshi2['item_info']

start_url = 'http://cq.58.com/pbdn/0/pn'

# spider 1
def get_onepage_links(page):
    url = start_url + str(page)
    print(url)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    for link in soup.select('a.t'):
        item_link = link.get('href').split('?')[0]
        if 'jump' in item_link.split('/'):
            pass
        else:
            print(item_link)
            item_links.insert_one({'link':item_link})

# spider 2
def get_detail(url):
    web_data = requests.get(url)
    if web_data.status_code == 200:
        soup = BeautifulSoup(web_data.text,'lxml')
        try:
            title = soup.select('h1.info_titile')[0].text
            price = soup.select('span.price_now i')[0].text
            area  = list(soup.select('div.palce_li  i')[0].text.split('-'))
            item_info.insert_one({'title':title,'price':price,'area':area})
        except:
            print('failed')

def get_npage_links(num):
    for n in range(1,num+1):
        get_onepage_links(n)



# get_onepage_links(1)
ex_url2= 'http://zhuanzhuan.58.com/detail/949501808509845510z.shtml'
ex_url = 'http://short.58.com/zd_p/6cbbf2bf-0523-4975-ab5a-814af11f0051/'

# get_detail(ex_url2)

