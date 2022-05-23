# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

# from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
# import logging

settings = get_project_settings()
class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.insert_one({'url': item['url'], 'title': item['title']}, dict(item))
        return item
        # log.msg("Question added to MongoDB database!",
        #         level=log.DEBUG, spider=spider)
