# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
from settings import IMAGES_STORE
import os
import pymongo


class DouyuImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # ImagesPipeline的get_media_requests方法

        yield scrapy.Request(item["image_link"])

    def item_completed(self, results, item, info):
        # 重写父类的item_completed方法 将图片改名
        image_path = [x['path'] for ok, x in results if ok]
        item['image_path'] = IMAGES_STORE + "full/" + item['nick_name'] + '.jpg'

        os.rename(IMAGES_STORE + image_path[0], item['image_path'])
        return item


class DouyuMongoDBPipeline(object):
    def __init__(self):
        # 连接本地mongoDB数据库
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        # 创建数据库Douyu
        self.db_name = self.client['Douyu']
        # 创建表DouyuDirector
        self.sheet_name = self.db_name['DouyuDirector']

    def process_item(self, item, spider):
        # 将item插入表
        self.sheet_name.insert(dict(item))
        return item
