# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from AQI.items import AqiItem
from datetime import datetime
class AqiSpider(CrawlSpider):
    
    name = "aqi"
    allowed_domains = ["aqistudy.cn"]
    start_urls = (
        'http://www.aqistudy.cn/historydata/',
    )

    rules = (
            # 提取城市的链接，返回该城市所有月份的响应
            Rule(LinkExtractor(allow=r"monthdata\.php\?city=")),  # 不写回调函数follow默认为True 
            # 提取每个月的链接，返回每一天的响应
            Rule(LinkExtractor(allow=r"daydata\.php\?city="),callback="parse_item")     
            ) 

    def parse_item(self, response):
        tr_list = response.xpath("//tr")
        item = AqiItem()
        # 城市名
        item["city"] = response.xpath("//h2/text()").extract_first()[8:-11 ]
        # 抓取时间
        item["utc_time"] = datetime.utcnow()
        # 数据源
        item["source"] = self.name
        # 每天的数据
        for tr in tr_list[1:]:
            # 日期
            item["date"] = tr.xpath("./td[1]/text()").extract()[0]
            # aqi指数
            item["aqi"] = tr.xpath("./td[2]/text()").extract()[0]
            # 质量等级
            item["level"] = tr.xpath("./td[3]/span/text()").extract()[0]
            # pm2.5含量
            item["pm2_5"] = tr.xpath("./td[4]/text()").extract()[0]
            # pm10含量
            item["pm10"] = tr.xpath("./td[5]/text()").extract()[0]
            # 二氧化硫含量
            item["so2"] = tr.xpath("./td[6]/text()").extract()[0]
            # 一氧化碳含量
            item["co"] = tr.xpath("./td[7]/text()").extract()[0]
            # 二氧化氮含量
            item["no2"] = tr.xpath("./td[8]/text()").extract()[0]
            # 臭氧含量
            item["o3"] = tr.xpath("./td[9]/text()").extract()[0]
        yield item 
