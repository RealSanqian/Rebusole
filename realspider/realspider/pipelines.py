# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import MySQLdb
import MySQLdb.cursors

#
# class RealspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
from twisted.enterprise import adbapi


class W3SchoolPipeline(object):
    def __init__(self):
        self.file = codecs.open('w3school_data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item

    def spider_closed(self, spider):
        self.file.close()


class InsertMysql(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            db='dbName',
                                            user='user',
                                            passwd='passoword',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False
                                            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
        # insert the data to databases                 #把数据插入到数据库中

    def _conditional_insert(self, tx, item):
        sql = "insert into real_spider (title,url)values (%s, %s)"
        tx.execute(sql, (item["blog_name"], item["blog_url"]))
