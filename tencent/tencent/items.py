# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()
    detail_link = scrapy.Field()
    position_type = scrapy.Field()
    employee_need = scrapy.Field()
    position_city = scrapy.Field()
    publish_times = scrapy.Field()
    position_duty = scrapy.Field()
    position_require = scrapy.Field()