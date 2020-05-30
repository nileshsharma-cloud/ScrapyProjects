# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author_name = scrapy.Field()
    all_tags = scrapy.Field()


class Amazon(scrapy.Item):
    book_title = scrapy.Field()
    book_price = scrapy.Field()
    book_author = scrapy.Field()
