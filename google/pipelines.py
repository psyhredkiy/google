# -*- coding: utf-8 -*-
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Urlpeline(object):
    def process_item(self, item, spider):
        itm = "".join(item['url]')
        p =r e.compile("(/url.*)(q=)(.*)(&sa.*)")
        url = re.sub(p,r"/3",)
        item['url'] = url
        return item
