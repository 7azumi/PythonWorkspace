from pyquery import PyQuery as pq

doc = pq(filename='test1.html')
items = doc('.footer')
print(items)