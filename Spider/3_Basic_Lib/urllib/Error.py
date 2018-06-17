from urllib import request,error

try:
    response = request.urlopen('https://www.cuiqingcai.com/indddex.html',timeout=0.1)
    print(response.read().decode('utf-8'))
except error.URLError as e:
    print(type(e.reason))
