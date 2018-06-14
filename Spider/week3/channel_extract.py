from bs4 import BeautifulSoup
import requests



start_url = 'http://cq.58.com/sale.shtml'

def get_channel_urls(url):
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text,'lxml')
    links_tail = soup.select('ul.ym-submnu > li > b > a')
    for link_tail in links_tail:
        link = 'http://cq.58.com' + link_tail.get('href')
        print(link)


channel_list = '''
http://cq.58.com/shouji/
http://cq.58.com/tongxunyw/
http://cq.58.com/danche/
http://cq.58.com/diandongche/
http://cq.58.com/fzixingche/
http://cq.58.com/sanlunche/
http://cq.58.com/peijianzhuangbei/
http://cq.58.com/diannao/
http://cq.58.com/bijiben/
http://cq.58.com/pbdn/
http://cq.58.com/diannaopeijian/
http://cq.58.com/zhoubianshebei/
http://cq.58.com/shuma/
http://cq.58.com/shumaxiangji/
http://cq.58.com/mpsanmpsi/
http://cq.58.com/youxiji/
http://cq.58.com/ershoukongtiao/
http://cq.58.com/dianshiji/
http://cq.58.com/xiyiji/
http://cq.58.com/bingxiang/
http://cq.58.com/jiadian/
http://cq.58.com/binggui/
http://cq.58.com/chuang/
http://cq.58.com/ershoujiaju/
http://cq.58.com/yingyou/
http://cq.58.com/yingeryongpin/
http://cq.58.com/muyingweiyang/
http://cq.58.com/muyingtongchuang/
http://cq.58.com/yunfuyongpin/
http://cq.58.com/fushi/
http://cq.58.com/nanzhuang/
http://cq.58.com/fsxiemao/
http://cq.58.com/xiangbao/
http://cq.58.com/meirong/
http://cq.58.com/yishu/
http://cq.58.com/shufahuihua/
http://cq.58.com/zhubaoshipin/
http://cq.58.com/yuqi/
http://cq.58.com/tushu/
http://cq.58.com/tushubook/
http://cq.58.com/wenti/
http://cq.58.com/yundongfushi/
http://cq.58.com/jianshenqixie/
http://cq.58.com/huju/
http://cq.58.com/qiulei/
http://cq.58.com/yueqi/
http://cq.58.com/bangongshebei/
http://cq.58.com/diannaohaocai/
http://cq.58.com/bangongjiaju/
http://cq.58.com/ershoushebei/
http://cq.58.com/chengren/
http://cq.58.com/nvyongpin/
http://cq.58.com/qinglvqingqu/
http://cq.58.com/qingquneiyi/
http://cq.58.com/chengren/
http://cq.58.com/xiaoyuan/
http://cq.58.com/ershouqiugou/
http://cq.58.com/tiaozao/
'''