# -*- coding: utf-8 -*-

import scrapy
import sys
import os
#to resolve module not found jdpaipai
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
print(ffpath)
sys.path.append(ffpath)

from scrapy.crawler import CrawlerProcess


from jdpaipai.spiders.auctionlist import AuctionlistSpider



class AuctionnavSpider(scrapy.Spider):
    name = 'auctionnav'
    allowed_domains = ['paipai.jd.com/auction-list']
    #revise http to https
    start_urls = ['https://paipai.jd.com/auction-list/']

    def parse(self, response):
        # pass
        print ("AuctionlistSpider start parse")

        

        os.system("scrapy crawl auctionlist " + response.url )
        process = CrawlerProcess()
        aclist = AuctionlistSpider()
        process.crawl(aclist)
        process.start() # the script will block here until all crawling jobs are finished

        







