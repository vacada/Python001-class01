# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmzdmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    phone_rank = scrapy.Field()
    phone_name = scrapy.Field()
    comment_link = scrapy.Field()
    phone_comment = scrapy.Field()
    comment_page = scrapy.Field()
