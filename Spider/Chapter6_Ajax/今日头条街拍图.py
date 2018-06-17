from urllib.parse import urlencode
import requests
import os
from hashlib import md5
from multiprocessing import Pool

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            try:
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    st = image.get('url')
                    yield {
                        'image': 'http:' + st.replace('list', 'origin'),
                        'title': title
                    }
            except: pass


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.jpg'.format(item.get('title'), md5(response.content).hexdigest())
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)

    except requests.ConnectionError:
        print('Failed to Save Image')

def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 10

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    map(main, groups)
    pool.close()
    pool.join()
