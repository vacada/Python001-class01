# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd
import csv
import pymysql
from smzdm.conndb import ConnDB

class SmzdmPipeline:
    def __init__(self):
        self.db = ConnDB()

    # 通过pymysql写入数据库
    def process_item(self, item, spider):
        self.db.run(item)
        return item
