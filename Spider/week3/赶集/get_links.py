from bs4 import BeautifulSoup
import requests
import pymongo


start_url = 'http://bj.ganji.com/wu/'
host_url = 'http://bi.ganji.com'


# 连接数据库
client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
group_links = ganji['group_links']

def get_group_links(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    links = soup.select('.fenlei > dt > a')

    for link in links:
        group_link = host_url + link.get('href')
        # group_links.insert_one({'group_link':group_link})
        print(group_link)


# get_group_links(start_url)

group_list = '''
http://bi.ganji.com/jiaju/
http://bi.ganji.com/rirongbaihuo/
http://bi.ganji.com/shouji/
http://bi.ganji.com/bangong/
http://bi.ganji.com/nongyongpin/
http://bi.ganji.com/jiadian/
http://bi.ganji.com/ershoubijibendiannao/
http://bi.ganji.com/ruanjiantushu/
http://bi.ganji.com/yingyouyunfu/
http://bi.ganji.com/diannao/
http://bi.ganji.com/xianzhilipin/
http://bi.ganji.com/fushixiaobaxuemao/
http://bi.ganji.com/meironghuazhuang/
http://bi.ganji.com/shuma/
http://bi.ganji.com/laonianyongpin/
http://bi.ganji.com/xuniwupin/
http://bi.ganji.com/qitawupin/
http://bi.ganji.com/ershoufree/
http://bi.ganji.com/wupinjiaohuan/
'''