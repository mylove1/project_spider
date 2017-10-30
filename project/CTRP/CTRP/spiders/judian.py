# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os
from CTRP.items import JudianItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class JudianSpider(CrawlSpider):
    name = 'judian'
    allowed_domains = ['ctrip.com']
    start_urls = ['http://hotels.ctrip.com/jiudian/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_start_url(self,response):
        all_city_node = response.xpath("//div[@class='index_item sec_province'][1]/dl")
        for node in all_city_node:
            item = JudianItem()
            # 省名
            try:
                item["province"] = node.xpath('./dt/a/@title')[0].extract()
            except:
                item["province"] = "直辖市与特别行政区"

            # 创建省名文件夹
            province_file = "./HotelData/" + item["province"]
            if not os.path.exists(province_file):
                os.makedirs(province_file)

            # 各个身城市名和城市链接列表
            item["city_name_list"] = node.xpath("./dd/a/@title").extract()
            item["city_link_list"] = node.xpath("./dd/a/@href").extract()
            for city_name,city_link in zip(item['city_name_list'],item['city_link_list']):
                # 创建城市名文件夹
                url = "http://hotels.ctrip.com" + city_link
                city_file = province_file + "/" + city_name
                if not os.path.exists(city_file):
                    os.makedirs(city_file)
                yield scrapy.Request(url,meta={"city_path": city_file,"item": item},callback=self.parse_second_url)    

        
    def parse_second_url(self,response):
        city_path = response.meta["city_path"]
        item = response.meta["item"]
        region_list = response.xpath("//div[@class='index_item'][1]//li")
        for node in region_list:
            # 取区名
            item["region_name"] = node.xpath("./a/@title")[0].extract()
            item["region_link"] = node.xpath("./a/@href")[0].extract()
            region_path = city_path + "/" + item["region_name"]
            if not os.path.exists(region_path):
                os.makedirs(region_path)





    def parse_item(self, response):
        pass
