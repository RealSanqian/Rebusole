# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item , Field

# class RealspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class W3schoolItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class CSDNBlogItem(Item):
    article_name = Field()
    article_url = Field()

class CsdnblogcrawlspiderItem(Item):
        blog_url = Field()
        blog_name = Field()