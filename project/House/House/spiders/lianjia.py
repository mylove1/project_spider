# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from House.items import LianJiaItem

class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    # 以北京链家为入口
    start_urls = ['http://bj.lianjia.com/']

    rules = (
        # 获取各城市二手房链接
        Rule(LinkExtractor(allow=r"http[s]?://\w+\.lianjia\.com/.*ershoufang/$")),
        # 获取房源详情页链接
        Rule(LinkExtractor(allow=r".*ershoufang/.*\.html$"),callback='parse_item',follow=False),
        # 获取页码链接
        Rule(LinkExtractor(allow=r".*ershoufang/pg\d+/$"),follow=True)
    )


    def parse_item(self, response):
        item = LianJiaItem()
        # 1.城市
        try:
            item["city"] = response.xpath("//div[@class='fl l-txt']/a/text()")[1].extract()[:-3]
        except:
            item["city"] = response.xpath("//em/text()")[0].extract()
        # 2.区名
        item["field"] = response.xpath("//div[@class='fl l-txt']/a/text()")[2].extract()[:-3]
        # 3.街道名
        item["street_name"] = response.xpath("//div[@class='fl l-txt']/a/text()")[3].extract()[:-3]
        # 4.房产名或小区名
        item["estate"] = response.xpath("//div[@class='fl l-txt']/a/text()")[4].extract()[:-3]
        # 5.总价
        item["total_price"] = response.xpath("//span[@class='total']/text()")[0].extract() + "w"
        # 6.每平米价
        item["m2_price"] = response.xpath("//div[@class='text']//span/text()")[0].extract() + "yuan/m2"
        # 费用
        #item["fee"] = response.xpath("//span[@class='taxtext']/@title")[0].extract() + response.xpath("//span[@id='PanelTax']/text()")[0].extract() + "w"
        # 7.建筑面积
        item["build_area"] = response.xpath("//div[@class='content']//li[3]/text()")[0].extract()
        # 8.套内面积
        item["house_area"] = response.xpath("//div[@class='content']//li[5]/text()")[0].extract()
        # 9.户型
        item["house_style"] = response.xpath("//div[@class='content']//li[1]/text()")[0].extract()
        # 10.楼层
        item["house_floor"] = response.xpath("//div[@class='content']//li[2]/text()")[0].extract()
        # 11.朝向
        item["house_direction"] = response.xpath("//div[@class='content']//li[7]/text()")[0].extract()
        # 12.装修情况
        item["house_decoration"] = response.xpath("//div[@class='content']//li[9]/text()")[0].extract()
        # 13.产权年限
        item["property_right"] = response.xpath("//div[@class='content']//li[12]/text()")[0].extract()
        # 房屋年限
        item["house_used"] = response.xpath("//div[@class='transaction']//li[5]/text()")[0].extract()
        # 14.核心卖点
        item["sele_power"] = response.xpath("//div[@class='content']/text()").extract()[10]
        # 房屋链接
        item['room_link'] = response.url
        yield item
