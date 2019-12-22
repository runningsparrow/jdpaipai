# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class JdpaipaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    _id = scrapy.Field()
    itemlink = scrapy.Field()
    itemimg = scrapy.Field()
    itemprice = scrapy.Field()
    itemorigprice = scrapy.Field()
    itemlabel = scrapy.Field()
    itemrepo = scrapy.Field()
    itemname = scrapy.Field()
    itemstatus = scrapy.Field()
    itemtime_desc = scrapy.Field()
    itemtime_hour = scrapy.Field()
    itemtime_minute = scrapy.Field()
    itemtime_second = scrapy.Field()
    itemtimestamp = scrapy.Field()
