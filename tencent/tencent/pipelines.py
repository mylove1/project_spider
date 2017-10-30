# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tencent.items import TencentItem
import json


class TencentPipeline(object):
    def __init__(self):
        # 创建一个文件并打开
        self.file = open("tencent.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            # 将传过来的item转化为字典并转化为json编码，再写入到文件，返回item给爬虫继续执行爬取函数
            content = json.dumps(dict(item))
            self.file.write(content + "," + "\n")
        return item

    def close_spider(self, spider):
        # 关闭文件
        self.file.close()
