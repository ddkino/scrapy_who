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
        print '----------- parse dataset /ROOT -------------'
        print response.meta
        # if not 'dataset_root' in response.meta['dataset_root']:
        #     response.meta['dataset_root'] = ""

        sel_iframe = response.xpath("//iframe").extract()
        print sel_iframe, len(sel_iframe)
        # if sel_iframe:
        #     print sel_iframe.extact()
        #     return
        for sel in response.xpath("//ul[contains(@class,'list_dash')]/li"):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()

            print '******************************'
            print link[0]
            print title[0]
            # url = response.xpath(link)
            # url = response.urljoin(link)
            # print url
            if link[0]:
                print '----------- dataset_root -------------'
                # if 'dataset_root' in response.meta:
                #     print response.meta['dataset_root'][0]+title[0]
                # else:
                #     dataset_root = title[0]
                dataset_root = title[0]
                url = "http://apps.who.int/gho/data/"+link[0];
                yield scrapy.Request(url, callback=self.parse, meta={'url': url, 'dataset_root': dataset_root})

            else:
                for sel in response.xpath("//ul[contains(@class,'list_dash')]/li"):
                    title = sel.xpath('a/text()').extract()
                    link = sel.xpath('a/@href').extract()
                    desc = sel.xpath('text()').extract()
                    print 'resources  ******************************'
                    print link[0]
                    print title[0]
            break

    def parse_dir_contents(self, response):

        print '----------- parse dataset /child/dataset_root -------------'
        print response.meta['dataset_root']
        print response.meta['url']
        print '----------- parse dataset /child/iframe -------------'
        sel_iframe = response.xpath("//iframe").extract()
        print sel_iframe
        print '----------- parse dataset /child/... -------------'
        for sel in response.xpath("//ul[contains(@class,'list_dash')]/li"):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc