# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # 商品链接
    goods_link = scrapy.Field()
    # 商品价格
    goods_price = scrapy.Field()
    # 商品标题
    goods_title = scrapy.Field()
    # 店铺
    goods_store = scrapy.Field()
    # 店铺链接
    store_link = scrapy.Field()
    # 评论数量
    comment_num = scrapy.Field()
