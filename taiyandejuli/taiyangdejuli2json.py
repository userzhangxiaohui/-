# coding:utf-8
import requests
from bs4 import BeautifulSoup
import json
#获取小说《太阳的距离》全部章节标题和链接，存入json
#Htmlparser读取json获取小说正文
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent': user_agent }
#获取包含所有章节链接的页面
r = requests.get('http://www.136book.com/taiyangdijuli/', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
content = []#存放获取的标题和href
for ols in soup.find_all(class_="clearfix"):
    for biaoti in ols.find_all('a'):
        href = biaoti.get('href')
        title = biaoti.string
        content.append({'title':title,'href':href})
with open('taiyangdejuli.json', 'w') as fp:
    json.dump(content,fp=fp, indent=4, ensure_ascii=False)
    #将获取的标题和链接存入json文件
