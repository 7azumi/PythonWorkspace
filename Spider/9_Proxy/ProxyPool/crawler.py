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

    def crawl_daili66(self, page_count=4):
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
        for i in range(1, 4):
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
        for page in range(1, 4):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s * 匹配空格，起到换行作用
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')

    def crawl_xicidaili(self):
        for page in range(1,3):
            start_url = 'https://www.xicidaili.com/nn/{}'.format(page)
            html = get_page(start_url)
            doc = pq(html)
            trs = doc('#ip_list tr:gt(0)').items()
            for tr in trs:
                ip = tr.find('td:nth-child(2)').text()
                port = tr.find('td:nth-child(3)').text()
                yield ':'.join([ip, port])

