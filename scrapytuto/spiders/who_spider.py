__author__ = 'DD'


import scrapy

import scrapy
class WhoSpider(scrapy.Spider):
    name = "who"
    allowed_domains = ["apps.who.int"]
    start_urls = [
    "http://apps.who.int/gho/data/node.main",
    #"http://apps.who.int/gho/data/node.home/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        print response.url.split("/")
        with open(filename, 'wb') as f:
            f.write(response.body)

        print '----------- parse dataset /ROOT -------------'
        for sel in response.xpath("//ul[contains(@class,'list_dash')]/li"):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc