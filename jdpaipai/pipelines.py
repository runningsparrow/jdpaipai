# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient


class JdpaipaiPipeline(object):
    def process_item(self, item, spider):
        return item


class auctionPipeline(object):

    def open_spider(self, spider):
        if spider.name == "auctionlist":
            print ("++++++++++++++++++")
            print ("open auctionlist")
            # 链接数据库
            self.mongoconn = MongoClient(host="127.0.0.1",port=27017,) #connect to mongodb
            #for prod
            # self.mongoconn.jdpaipai1.authenticate("sparrow","123456")  #auth
            # self.jdpaipaidb = self.mongoconn.jdpaipai1
            #for dev
            self.mongoconn.jdpaipai1test1.authenticate("sparrow","123456")  #auth
            self.jdpaipaidb = self.mongoconn.jdpaipai1test1

            print ("++++++++++++++++++")

    def process_item(self, item, spider):
        if spider.name == "auctionlist":
            # print ("start process auctionPipeline")
            # print (">>>>>>>>>>>>>>>>>>>>>>>>>>")
            print (item)
            # print ("<<<<<<<<<<<<<<<<<<<<<<<<<<")


    
            # 写入数据库
            self.jdpaipaidb.jdpaipai1.insert(item)

        return item

    def close_spider(self,spider):

      #关闭连接
        if spider.name == "auctionlist":
            print ("clsee auctionlist")