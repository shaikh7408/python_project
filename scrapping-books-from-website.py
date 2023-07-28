import requests
from bs4 import BeautifulSoup

PAGE=requests.get('http://www.example.com')
soup=BeautifulSoup(PAGE.content,'html.parser')
print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])
print(PAGE.content)
