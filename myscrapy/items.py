# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClassifyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()


class NovelUrlItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    classify = scrapy.Field()
    author = scrapy.Field()
    status = scrapy.Field()
    summary = scrapy.Field()
    image = scrapy.Field()
    latest = scrapy.Field()


class ChapterItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
