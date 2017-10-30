# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]
    offset = 0
    # 手机app端ajax链接
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    # 初始链接
    start_urls = (
        base_url + str(offset),
    )

    def parse(self, response):
        # 将data下的json格式转化为python
        data_list = json.loads(response.body)['data']

        if not data_list:
            return
        for data in data_list:
            item = DouyuItem()
            # 获取房间链接
            item["room_link"] = "http://www.douyu.com/" + data["room_id"]
            # 图片链接
            item["image_link"] = data["vertical_src"]
            # 主播艺名
            item["nick_name"] = data["nickname"]
            # 主播所在城市
            item["anchor_city"] = data["anchor_city"]

            yield item  # 返回给引擎，引擎再给管道处理
        # offsetj+20 拼接链接发送下个链接请求
        self.offset += 20
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)
