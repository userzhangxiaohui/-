# coding: utf-8

import re
from bs4 import BeautifulSoup
from urllib import parse

class HtmlParse(object):

    def parser(self, page_url, html_cont):
        '''
        解析网页内容，抽取url和数据
        pag_url: 下载页面的url
        html_cont: 下载的网页内容
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的url集合
        page_url: 下载页面的url
        '''
        new_urls = set()
        #摘要中的相关词条在class=="lemma-summary"中，获取该tag下的所有<a>元素
        links = soup.find('div', class_="lemma-summary").find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''抽取有效数据'''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data
    



