# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from myscrapy.items import *
import pymysql


class MyscrapyPipeline(object):
    def __init__(self):
        # 建立数据库连接
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='novel',
                                          charset='utf8')
        # 创建操作游标
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        if isinstance(item, ClassifyItem):
            self.cursor.execute("select * from classify where name='%s'" % (item["name"]))
            data = self.cursor.fetchone()
            if (data == None):
                self.cursor.execute("insert into classify (name,url) values ('%s','%s')" % (item["name"], item["url"]))
                self.connection.commit()
        if isinstance(item, NovelUrlItem):
            self.cursor.execute("select * from novel where url='%s'" % (item["url"]))
            data = self.cursor.fetchone()
            if (data == None):
                print("2")
                scrapy.Request(item["url"], callback=spider.getNovelInfo)
        return item

    def __del__(self):
        # 关闭操作游标
        self.cursor.close()
        # 关闭数据库连接
        self.connection.close()
