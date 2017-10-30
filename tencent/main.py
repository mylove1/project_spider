# usr/bin/python3
# coding=utf-8
from scrapy import cmdline


def main():
    # 相当与命令行的scrapy crawl tencent
    cmdline.execute("scrapy crawl tencent_spider".split())


if __name__ == "__main__":
    main()
