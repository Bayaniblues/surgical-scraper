# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SurgtechItem(scrapy.Item):
    scraped_question = scrapy.Field()
    scraped_answer = scrapy.Field()

    pass
