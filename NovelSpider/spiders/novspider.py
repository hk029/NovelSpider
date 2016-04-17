# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from NovelSpider.items import NovelspiderItem

class NovspiderSpider(scrapy.Spider):
    name = "novspider"
    allowed_domains = ["daomubiji.com/"]
    start_urls = (
        'http://www.daomubiji.com/',
    )

    def parse(self, response):
        # print response.body
        selector = Selector(response)
        tables = selector.xpath('//table')
        for each in tables:
            print
            bookName = each.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
            url = each.xpath('tr/td/a/@href').extract()
            name = each.xpath('tr/td/a/text()').extract()
            for i in range(len(url)):
                item = NovelspiderItem()
                item['bookName'] = bookName
                item['chapterURL'] = url[i]
                try:
                    item['bookTitle'] = name[i].split(' ')[0]
                    item['chapterNum'] = name[i].split(' ')[1]
                except Exception,e:
                    continue
                try:
                    item['chapterName'] = name[i].split(' ')[2]
                except Exception,e:
                    item['chapterName'] = name[i].split(' ')[1][-3]
                print item
                yield item


