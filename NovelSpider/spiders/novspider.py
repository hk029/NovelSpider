# -*- coding: utf-8 -*-
import scrapy


class NovspiderSpider(scrapy.Spider):
    name = "novspider"
    allowed_domains = ["http://www.daomubiji.com/"]
    start_urls = (
        'http://www.http://www.daomubiji.com//',
    )

    def parse(self, response):
        pass
