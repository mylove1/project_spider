# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 城市名
    city = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # AQI指数
    aqi = scrapy.Field()
    # 质量等级
    level = scrapy.Field()
    # PM2.5
    pm2_5  = scrapy.Field()
    # PM10
    pm10 = scrapy.Field()
    # 二氧化硫
    so2 = scrapy.Field()
    # 一氧化碳
    co = scrapy.Field()
    # 二氧化氮
    no2 = scrapy.Field()
    # 臭氧
    o3 = scrapy.Field()

    # 数据抓取时间
    utc_time = scrapy.Field()
    # 数据源
    source = scrapy.Field()
