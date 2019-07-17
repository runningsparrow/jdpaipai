# -*- coding: utf-8 -*-
import scrapy

from jdpaipai.items import JdpaipaiItem
import os
import time

class AuctionlistSpider(scrapy.Spider):
    name = 'auctionlist'
    allowed_domains = ['paipai.jd.com/auction-list/']
    start_urls = ['https://paipai.jd.com/auction-list/']

    #for loop
    nextpage = 1;
    totalpage = 0;

    def parse(self, response):
        # pass
        print ("AuctionlistSpider start parse")

        # print(response.body)
        #parse
        
        auctionlist = response.xpath('//div[@id="plist"]/ul[@class="gl-wrap"]/li')
        print(len(auctionlist))
        for item in auctionlist:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(item)
            jditem = JdpaipaiItem()
            itemlink = item.xpath('div/div[@class="p-img"]/a/@href').extract()
            print(itemlink)

            #取 itemlink中的给 _id 赋值
            itemno = itemlink[0].split('/')[2]
            jditem['_id'] = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) + itemno

            #注意 xpath 返回的是数组，需要通过下标取出
            jditem['itemlink'] = itemlink[0]

            itemimg = item.xpath('div/div[@class="p-img"]/a/img/@src').extract()
            jditem['itemimg'] = itemimg[0]


            itemprice = item.xpath('div/div[@class="p-price"]/i/text()').extract()
            print(itemprice)
            jditem['itemprice'] = itemprice[0]

            itemorigprice = item.xpath('div/div[@class="p-price"]/span[@class="origin-price"]/text()').extract()
            print(itemorigprice)
            jditem['itemorigprice'] = itemorigprice[0]

            itemlabel = item.xpath('div/div[@class="p-label"]/span[last()]/text()').extract()
            print(itemlabel)
            jditem['itemlabel'] = itemlabel[0]
            
            itemrepo = item.xpath('div/div[@class="p-label"]/span/text()').extract()
            print(itemrepo)
            jditem['itemrepo'] = itemrepo[0]

            itemname = item.xpath('div/div[@class="p-name"]/a/@title').extract()
            print(itemname)
            jditem['itemname'] = itemname[0]

            itemstatus  = item.xpath('div/div[@class="p-btn"]/a/text()').extract()
            print(itemstatus)
            jditem['itemstatus']= itemstatus[0]


            jditem['itemtimestamp'] = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            print(jditem['itemtimestamp'])

            print("********************************************")
            # 将item提交给管道
            yield jditem
            print("********************************************")


        #next urls process
        # checklast = response.xpath('//button[(@class="btn-next") and not(@disabled)]')
        checklast = response.xpath('//button[(@class="btn-next") and (@disabled="disabled")]')
        print(checklast)
        if len(checklast)==0:
            print("Please vist next page!")
            print(response.url)
            yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=True)
        else:
            print("This is the last page!")


#代替命令行执行爬虫
if __name__ == '__main__':
    os.system("scrapy crawl auctionlist")