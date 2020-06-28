# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas
import csv

class MaoyanPipeline:
#     def process_item(self, item, spider):
#         return item

    # 通过pandas写入数据
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_tag = item['movie_tag']
        movie_time = item['movie_time']
        data = {
                '电影名称': movie_name,
                '类型': movie_tag,
                '上映时间': movie_time,
        }
        movie_data = pandas.DataFrame(data=data)
        movie_data.to_csv('./movie.csv', encoding='utf8', index=False)
        return item
    

