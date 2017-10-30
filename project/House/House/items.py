# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianJiaItem(scrapy.Item):
    # 1.城市名
    city = scrapy.Field()
    # 2.区名
    field = scrapy.Field()
    # 3.街道名
    street_name = scrapy.Field()
    # 4.房产名或小区名
    estate = scrapy.Field()
    # 5.总价
    total_price = scrapy.Field()
    # 6.每平米价
    m2_price = scrapy.Field()
    # 费用
    fee = scrapy.Field()
    # 7.建筑面积
    build_area = scrapy.Field()
    # 8.套内面积
    house_area = scrapy.Field()
    # 9.户型
    house_style = scrapy.Field()
    # 10.楼层
    house_floor = scrapy.Field()
    # 11.朝向
    house_direction = scrapy.Field()
    # 12.装修情况
    house_decoration = scrapy.Field()
    # 13.产权年限
    property_right = scrapy.Field()
    # 房屋年限
    house_used = scrapy.Field()
    # 14.核心卖点
    sele_power = scrapy.Field()
    # 链接
    room_link = scrapy.Field()
