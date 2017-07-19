# -*- coding: utf-8 -*-
import scrapy

class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    cimage_urls = scrapy.Field()
    cimages = scrapy.Field()