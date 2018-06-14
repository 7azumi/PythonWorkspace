from multiprocessing import Pool

from get_links import group_list
from url_parser import get_pages_item_links,get_info,item_list,item_info

def get_all_links_from(channel):
    for i in range(1,100):
        print(i)
        get_pages_item_links(channel,i)

def get_rest_link():
    in_link = [i['url'] for i in item_info.find()]
    un_link = [i['item_url'] for i in item_list.find()]
    x = set(in_link)
    y = set(un_link)
    return y-x



if __name__ == '__main__':
    pool = Pool()
    rest_urls = get_rest_link()
    # info_links = [i['item_url'] for i in item_list.find()]
    pool.map(get_info,rest_urls)
