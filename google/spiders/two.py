# -*- coding: utf-8 -*-
import scrapy
from google.items import GoogleItem


class TwoSpider(scrapy.Spider):
    name = "two"
    allowed_domains = ["google.com"]
    start_urls = ['https://www.google.com.ua/search?q=meine+liebe+site%3Afacebook.com&lr=lang_ru&biw=1920&bih=923&source=lnt&tbs=lr%3Alang_1ru%2Ccdr%3A1%2Ccd_min%3A12%2F1%2F2016%2Ccd_max%3A12%2F31%2F2016&tbm=#lr=lang_ru&tbs=lr:lang_1ru%2Ccdr:1%2Ccd_min:12%2F1%2F2016%2Ccd_max:12%2F31%2F2016&q=meine+liebe+site:facebook.com']


    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        results = sel.xpath('//div[@class="g"]')
        items = []
        for result in results:
            item = GoogleItem()
            item['url'] = result.xpath('//h3[@class="r"]/a/@href').extract()
            items.append(item)

        for item in items:
            yield item
