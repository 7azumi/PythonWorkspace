# -*- coding: utf-8 -*-

from utils import get_page
import re
from pyquery import PyQuery as pq
from time import sleep

class ProxyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class Crawler(object, metaclass=ProxyMetaClass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('Get Proxy Successfully, ', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=7):
        """
        Get proxies from daili66
        :param page_count: Page number
        :return: proxy
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count+1)]
        for url in urls:
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_kuaiproxy(self):
        for i in range(1, 7):
            url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(url)
            doc = pq(html)
            trs = doc('.table tbody tr').items()
            for tr in trs:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])
            sleep(1)
    def crawl_ip3366(self):
        for page in range(1, 7):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            if html:
                ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
                # \s * 匹配空格，起到换行作用
                re_ip_address = ip_address.findall(html)
                for address, port in re_ip_address:
                    result = address + ':' + port
                    yield result.replace(' ', '')

    def crawl_xicidaili(self):
        for page in range(1,5):
            start_url = 'https://www.xicidaili.com/nn/{}'.format(page)
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host':'www.xicidaili.com',
                'Referer':'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests':'1',
            }
            html = get_page(start_url,options=headers)
            if html:
                doc = pq(html)
                trs = doc('#ip_list tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(2)').text()
                    port = tr.find('td:nth-child(3)').text()
                    yield ':'.join([ip, port])

