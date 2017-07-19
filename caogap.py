import requests
from bs4 import BeautifulSoup
import re

headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

url = 'http://jandan.net/pic'

soup = BeautifulSoup(requests.get(url, headers=headers).text,'html.parser')
print(soup.prettify())