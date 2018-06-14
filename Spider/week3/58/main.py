from multiprocessing import Pool
from pbdn_58 import item_links
from pbdn_58 import get_detail

import time


if __name__ == '__main__':
    op = time.time()
    pool = Pool()

    urls = []
    for url in item_links.find():
        urls.append(url['link'])

    # print(len(urls))

    pool.map(get_detail,urls)
    print('get successful!')


    ed = time.time()
    print(ed-op)