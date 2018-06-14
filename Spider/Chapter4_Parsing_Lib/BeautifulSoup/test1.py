from bs4 import BeautifulSoup
html = '<p class="point" id="pt">Point</p>'
soup = BeautifulSoup(html, 'lxml')
print(soup.p.attrs)