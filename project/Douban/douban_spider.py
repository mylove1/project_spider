#! /usr/bin/env python
# coding:utf-8
import requests
import Queue
from lxml import etree
from user_agent import generate_user_agent as ua
import random
import gevent
from gevent import monkey
monkey.patch_all()

class DoubanSpider(object):
    def __init__(self):
        self.data_queue = Queue.Queue()
        self.base_url = "http://movie.douban.com/top250?start="
        # 随即生成一百个user-agent 从中随机取出一个
        self.user_agent_list = [ua(os=('win','linux','mac')) for i in range(100)]
        self.headers = {"User-Agent": random.choice(self.user_agent_list )}
        self.num = 0
        self.total166_score = 0

    def start_work(self):
        # 每页25条数据由start参数决定，所以翻页就+25最后一页num要取到255
        url_list = [self.base_url + str(num) for num in range(0, 256, 25)]
        
        job_list = [gevent.spawn(self.parse_page,url) for url in url_list]
        gevent.joinall(job_list)


        while not self.data_queue.empty():
            print data_queue.get()
        # 打印看有多少条数据,前166个movie的评分
        print "已经爬取%d条数据" %self.num
        print "前166个电影评分的总分为%d" %self.total166_score

    def parse_page(self,url):
        # 调用加载函数发送请求
        html = self.load_page(url)
        html_node = etree.HTML(html)


        node_list = html_node.xpath("//div[@class='item']")

        for node in node_list:
            # 标题
            movie_title = node.xpath(".//span[@class='title']/text()")[0]
            # 评分
            movie_score = node.xpath(".//span[@class='rating_num']/text()")[0]
            # 序号
            movie_num= node.xpath(".//em/text()")[0]
           
            self.num += 1
            print "---"*10
            print "电影排名:%s"%movie_num
            print movie_title
            print movie_score
             
            if int(movie_num) <= 166:
                self.total166_score += float(movie_score)


    def load_page(self,url):
        html = requests.get(url,headers = self.headers).content
        
        return html


if __name__ == "__main__":
    # 实例化爬虫对象
    douban = DoubanSpider()
    douban.start_work()

