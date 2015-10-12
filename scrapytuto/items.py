# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytutoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DatasetItem(scrapy.Item):
     # dict_keys(['uri', 'description', 'id', 'title', 'resources', 'organization', 'owner'])
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
