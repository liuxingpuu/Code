# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WeatherItem(scrapy.Item):
    city = scrapy.Field()
    date = scrapy.Field()
    dayDesc = scrapy.Field()
    dayTemp = scrapy.Field()
