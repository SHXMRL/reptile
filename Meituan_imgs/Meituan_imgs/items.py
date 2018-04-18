# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanImgsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    addr=scrapy.Field()
    av_score=scrapy.Field()
    level=scrapy.Field()

    page_url=scrapy.Field()
    hotel_url=scrapy.Field()

    telephone=scrapy.Field()
    message=scrapy.Field()
    introduce=scrapy.Field()

    price=scrapy.Field()
    common=scrapy.Field()
    url=scrapy.Field()

    img_url=scrapy.Field()
    image_paths=scrapy.Field()
    images=scrapy.Field()
