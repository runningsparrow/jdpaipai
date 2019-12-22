# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time


class searchitem:

    def __init__(self):
        self.name = "searchitem"

    def mongodbconn(self,host,port,username,userpass):
        # 链接数据库
        self.mongoconn = MongoClient(host="127.0.0.1",port=27017,) #connect to mongodb
        #for prod
        # self.mongoconn.jdpaipai1.authenticate("sparrow","123456")  #auth
        # self.jdpaipaidb = self.mongoconn.jdpaipai1
        #for dev
        self.mongoconn.jdpaipai1test1.authenticate("sparrow","123456")  #auth
        self.jdpaipaidb = self.mongoconn.jdpaipai1test1
        return self.jdpaipaidb
        

    def searchbyname(self,collection,itemname):
        # result = self.jdpaipaidb.getCollection(collection).find({"itemname":{"$regex":itemname}})
        itemtime = time.strftime('%Y%m%d',time.localtime(time.time()))
        collection1 = self.jdpaipaidb[collection]
        result = collection1.find({"$and":[{"itemname":{"$regex":itemname}},{"itemtimestamp":{"$regex":itemtime}}]})
        # result = self.jdpaipaidb.jdpaipai1.find({"$and":[{"itemname":{"$regex":itemname}},{"itemtimestamp":{"$regex":itemtime}}]})
        print(result)
        print("debug1")
        for one in result:
            print(one)
        return result
    

if __name__ == '__main__':
    sritem = searchitem()
    host = "127.0.0.1"
    port = 27017
    username = "sparrow"
    userpass = "123456"
    collection = "jdpaipai1"

    sritem.mongodbconn(host,port,username,userpass)
    itemname = "Xbox"
    collection = 'jdpaipai1'
    # itemname = "索尼"
    # itemname = "变形金刚"
    sritem.searchbyname(collection,itemname)
