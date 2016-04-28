# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector
from DoubleColorBall.items import DoubleColorBallItem

class DoublecolorballSpider(scrapy.Spider):
    name = "DoublecolorballSpider"
    allowed_domains = ["datachart.500.com"]
    start_urls = (
        'http://datachart.500.com/dlt/history/newinc/history.php?start=30000&end=00000',
    )

    def parse(self, response):
        self.logger.info('DoublecolorballSpider Parse function called on %s', response.url)
        items = []
        sel = Selector(response)
        allItems = sel.css('tr.t_tr1')
        self.logger.info('DoublecolorballSpider selectItems count = %s', len(allItems))
        for index in range(1, len(allItems)):
            item = DoubleColorBallItem()
            item['issue'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[0]
            item['redBall1'] = allItems[index].css('td.cfont2').xpath('text()').extract()[0]
            item['redBall2'] = allItems[index].css('td.cfont2').xpath('text()').extract()[1]
            item['redBall3'] = allItems[index].css('td.cfont2').xpath('text()').extract()[2]
            item['redBall4'] = allItems[index].css('td.cfont2').xpath('text()').extract()[3]
            item['redBall5'] = allItems[index].css('td.cfont2').xpath('text()').extract()[4]
            item['blueBall1'] = allItems[index].css('td.cfont4').xpath('text()').extract()[0]
            item['blueBall2'] = allItems[index].css('td.cfont4').xpath('text()').extract()[1]
            item['poolBonus'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[1]
            item['firstNotes'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[2]
            item['firstBonus'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[3]
            item['secondNotes'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[4]
            item['secondBonus'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[5]
            item['totalBetting'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[6]
            item['date'] = allItems[index].css('td.t_tr1').xpath('text()').extract()[7]
            yield item
            # items.append(item)
        # return items