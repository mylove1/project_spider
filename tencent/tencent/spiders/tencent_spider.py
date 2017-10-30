# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class TencentSpiderSpider(CrawlSpider):
    name = 'tencent_spider'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0']

    rules = (
         Rule(LinkExtractor(allow=r"position\.php\?&start="), callback = "parse_item", follow = True),
    )

    def parse_item(self, response):

        item = TencentItem()
        for node in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            try:
                item["position_name"] = node.xpath(".//a/text()").extract()[0]
                item["detail_link"] = "http://hr.tencent.com/" + node.xpath(".//a/@href").extract()[0]
                item["position_type"] = node.xpath("./td[2]/text()").extract()[0]
                item["employee_need"] = node.xpath("./td[3]/text()").extract()[0]
                item["position_city"] = node.xpath("./td[4]/text()").extract()[0]
                item["publish_times"] = node.xpath("./td[5]/text()").extract()[0]
            except Exception as e:
                print e

            yield scrapy.Request(item["detail_link"], meta={"position_item": item}, callback=self.parse_position)

    def parse_position(self, response):
        item = response.meta["position_item"]
        item["position_duty"] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()[0]
        item["position_duty"] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()[0]
        yield item
