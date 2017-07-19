# *- coding:utf-8 -*
import requests
from bs4 import BeautifulSoup
import os
import re

#设置headers
headers = {
    'referer': 'http://jandan.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}

rootfile = r'C:\Users\zhang\Pictures\jandan'

def save_pic(res_url):
    global rootfile
    index = 0
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)
    page = get_page(html)
    for link in html.find_all('a', class_='view_img_link'):
        with open('{}\{}-{}.{}'.format(rootfile, page, index, link.get('href')[-3:]), 'wb') as savepic:
            savepic.write(requests.get("http:" + link.get('href')).content)
            index += 1

def get_page(html):
    page = html.find('span', class_='current-comment-page').string[1:-1]
    return page

if __name__ =='__main__':
    #从上次中断位置开始继续爬取
    url = 'http://jandan.net/pic/page-862#comments'
        
    for i in range(862):
        save_pic(url)
        url = BeautifulSoup(requests.get(url, headers=headers).text).find('a', {'class': 'previous-comment-page'}).get('href')


    #从最新一页开始爬取
    #url = 'http://jandan.net/pic'
    #max_pages = get_page(BeautifulSoup(requests.get(url, headers=headers).text))
    #for i in range(int(max_pages-869)):
        #save_pic(url)
        #url = BeautifulSoup(requests.get(url, headers=headers).text).find('a', {'class': 'previous-comment-page'}).get('href')
