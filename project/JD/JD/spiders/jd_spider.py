# -*- coding: utf-8 -*-
import scrapy
import urllib
from JD.items import JdItem

class JdSpiderSpider(scrapy.Spider):
    name = 'jd_spider'
    allowed_domains = ['jd.com']

    key = raw_input("请输入需要爬取的商品类:")
    page = 1
    kw ={"keyword": key}
    keyword = urllib.urlencode(kw)
    base_url = "https://search.jd.com/Search?&enc=utf-8&scrolling=y&page="
    start_urls = [base_url + str(page) + "&" + keyword]
    

    def parse(self,response):
        if self.page > 200:
            print "数据已更新"
            return
        print "------开始爬取第%s页"%self.page
        node_list = response.xpath("//div[@class='gl-i-wrap']")
        print "共有%d条商品数据"%len(node_list)
        for node in node_list:
            item = JdItem()
            item["goods_link"] = node.xpath("./div[@class='p-img']/a/@href")[0].extract()
            try:
                item["goods_price"] = node.xpath("./div[@class='p-price']//i/text()")[0].extract()
            except:
                item["goods_price"] = node.xpath("./div[@class='p-price']//strong/@data-price")[0].extract()
            try:
                item["goods_title"] = node.xpath("./div[@class='p-name p-name-type-2']//em/text()")[0].extract()
            except:
                item["goods_title"] = None
            try:
                item["goods_store"] = node.xpath("./div[@class='p-shop']//a/@title")[0].extract()
            except:
                item["goods_store"] = None
            try:
                item["store_link"] = node.xpath("./div[@class='p-shop']//a/@href")[0].extract()
            except:
                item["store_link"] = None
            try:
                item["comment_num"] = node.xpath("./div[@class='p-commit']//a/text()")[0].extract()
            except:
                item["comment_num"] = None
            yield item
        self.page += 1
        yield scrapy.Request(self.base_url + str(self.page) + "&" + self.keyword,callback=self.parse)

