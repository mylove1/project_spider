# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JdMongoDBPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=127.0.0.1,port=27017)
        self.
    def process_item(self, item, spider):
        
