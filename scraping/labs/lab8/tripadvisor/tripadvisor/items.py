# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HotelItem(scrapy.Item):
    name = scrapy.Field()
    review = scrapy.Field()
    reviewCount = scrapy.Field()