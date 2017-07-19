# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserInfoItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field()
    user_image_url = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    business = scrapy.Field()
    gender = scrapy.Field()
    employment = scrapy.Field()
    position = scrapy.Field()
    education = scrapy.Field()
    followees_num = scrapy.Field()
    followers_num = scrapy.Field()

class RelationItem(scrapy.Item):
    user_id = scrapy.Field()
    relation_type = scrapy.Field()
    relation_id = scrapy.Field()
