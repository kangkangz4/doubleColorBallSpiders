# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class LotteryPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.maxIssue = None
        self.getMaxIssue()

    # 获取最大期数
    def getMaxIssue(self):
        # 查出来的是个数组
        cursor = self.collection.find().sort('issue', pymongo.DESCENDING).limit(1)
        if cursor.count() > 0:
            maxIssueItem = cursor.next()
            # log.msg("LotteryPipeline maxIssueItem %s", maxIssueItem, level=log.DEBUG)
            # 判断当前查出的项目中是否包含期号
            if maxIssueItem.has_key('issue'):
                self.maxIssue = maxIssueItem['issue']
            # log.msg("LotteryPipeline maxIssue %s", self.maxIssue, level=log.DEBUG)

    def process_item(self, item, spider):
        valid = True
        insert = False
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        # 如果没有最大期号
        if self.maxIssue is None:
            insert = True
        else:
            # 数据库最大期号小于当前期号
            if int(self.maxIssue) < int(item['issue']):
                insert = True

        if valid and insert:
            self.collection.insert(dict(item))
            log.msg("LotteryPipeline added to MongoDB dataBase!", level=log.DEBUG, spider=spider)

        return item
