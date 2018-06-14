import requests,random

ip_list = [
    '115.223.238.186:9000',
    '115.218.127.62',
    '118.122.187.184',
    '115.218.126.138'
]

proxy_ip = random.choice(ip_list)

base_url = 'http://www.baidu.com'

proxies = {
    'http':proxy_ip
}

web_data = requests.get(base_url,proxies=proxies)
print(web_data)