import scrapy
from myscrapy.items import *


class QswSpider(scrapy.spiders.Spider):
    name = "qsw"
    allowed_domains = ["www.quanshuwang.com"]
    start_urls = ["http://www.quanshuwang.com/"]

    def parse(self, response):
        x_a = response.xpath('//ul[@class="channel-nav-list"]//a')
        for sel in x_a:
            name = sel.xpath('text()').extract_first()
            href = sel.xpath('@href').extract_first()
            yield ClassifyItem(name=name, url=href)
            yield scrapy.Request(href, callback=self.getInfo)

    def getInfo(self, response):
        x_a = response.xpath('//ul[@class="seeWell cf"]//a[@class="readTo"]')
        for sel in x_a:
            url = sel.xpath('@href').extract_first()
            yield scrapy.Request(url, callback=self.getNovelInfo)

    def getNovelInfo(self, response):
        print("1")
