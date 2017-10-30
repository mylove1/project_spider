# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JudianItem(scrapy.Item):
    # 各个省名和直辖市与特别行政区
    province = scrapy.Field()
    # 省下面的各个城市名和城市链接列表
    city_name_list = scrapy.Field()
    city_link_list = scrapy.Field()

    # 地区名
    region_name = scrapy.Field()
    # 地区链接
    region_link = scrapy.Field()
