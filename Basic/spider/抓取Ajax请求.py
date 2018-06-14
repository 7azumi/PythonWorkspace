import urllib.request
import json
import ssl


url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20'

def ajaxspider(url):
    req = urllib.request.Request(url)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    jsonStr = response.read().decode('utf-8')
    jsonData = json.loads(jsonStr)

    return jsonData


info = ajaxspider(url)
print(info)