# 取得xhr请求的url
from urllib.parse import urlencode
import requests
from pymongo import MongoClient
base_url = 'https://movie.douban.com/j/chart/top_list?'

headers = {
    'User-Agent': 'Chrome/66.0.3359.170',
    'X-Requested-With': 'XMLHttpRequest',
}

client = MongoClient('localhost', 27017)
douban = client['douban']
drama = douban['drama']

# 获得一页的json内容
def get_page(page):
    params = {
        'type': 11,
        'interval_id': '100:90',
        'start': page*20,
        'limit': 20
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("Error", e.args)

def parse_page(items):
    print(type(items))

def save_to_mongo(items):
    drama.insert_many(items)

items = get_page(0)
save_to_mongo(items)