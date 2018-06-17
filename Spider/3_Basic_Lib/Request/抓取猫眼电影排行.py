import re
import requests
from requests.exceptions import RequestException
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/66.0.3359.170 Safari/537.36'
}


def get_one_page(offset=0):
    url = 'http://maoyan.com/board/4/?offset={}'.format(offset)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except RequestException:
        return None


def parser_one_page(content):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"'
                         '.*?title="(.*?)".*?star">(.*?)</.*?time">(.*?)</'
                         '.*?integer">(.*?)</.*?fraction">(.*?)</', re.S)
    # print(res.text)
    items = re.findall(pattern, content)

    for item in items:
        yield {
            'index': item[0],
            'name': item[2].strip(),
            'image': item[1],
            'star': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('Top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# for item in get_one_page(10):
#     write_to_file(item)

if __name__ == '__main__':
    # 获取前10页电影排名(Top100)
    for num in range(0,11):
        page_data = get_one_page(num*10)
        for item in parser_one_page(page_data):
            write_to_file(item)