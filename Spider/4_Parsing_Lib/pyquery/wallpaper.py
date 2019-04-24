# 抓取bing当日高清壁纸
import requests
from pyquery import PyQuery as pq
from time import sleep

# 1.获取图片链接
r = requests.get('https://cn.bing.com/')
content = pq(r.text)    # 使用Pyquery解析html
jpg_url = 'https://cn.bing.com/' + content('#bgLink').attr('href')  # 查找到相应节点，并把节点属性中的地址传给图片链接对象
print(jpg_url)

# 2.下载图片
jpg = requests.get(jpg_url)
name = 'E:\wallpaper\simple desk\\' + jpg_url.split('/')[-1].split('_')[0] + '.jpg'  # 图片名称
name = name.replace('th?id=OHR.', '')
print(name)
with open(name, 'wb') as f: # 保存图片
    f.write(jpg.content)
print("\n\n        <(￣︶￣)>")
sleep(1)
