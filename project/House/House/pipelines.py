# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json


class HouseSavePipeline(object):
    def __init__(self):
        self.file = open("ershoufang.json","w")

    def process_item(self,item,spider):
        self.file.write(json.dumps(dict(item)) + ",\n")
        return item
    def close_spider(self,spider):
        self.file.close()

class HouseMongoDBPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1',port = 27017)
        self.db = self.client.LianJia
        self.collection = self.db.ershoufang
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
