# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 双色球
class DoubleColorBallItem(scrapy.Item):
    issue = scrapy.Field()           #期号
    redBall1 = scrapy.Field()        #红球1
    redBall2 = scrapy.Field()        #红球2
    redBall3 = scrapy.Field()        #红球3
    redBall4 = scrapy.Field()        #红球4
    redBall5 = scrapy.Field()        #红球5
    blueBall1 = scrapy.Field()       #绿球1
    blueBall2 = scrapy.Field()       #绿球2
    poolBonus = scrapy.Field()       #奖池奖金
    firstNotes = scrapy.Field()      #一等奖注数
    firstBonus = scrapy.Field()      #一等奖金额
    secondNotes = scrapy.Field()     #二等奖注数
    secondBonus = scrapy.Field()     #二等奖金额
    totalBetting = scrapy.Field()    #总投注金额
    date = scrapy.Field()            #开奖日期
