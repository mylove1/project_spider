# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    room_link = scrapy.Field()
    image_link = scrapy.Field()
    nick_name = scrapy.Field()
    anchor_city = scrapy.Field()

    # 图片在磁盘的路径
    image_path = scrapy.Field()