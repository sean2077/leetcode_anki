# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionDataItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    submission_list = scrapy.Field()
    topics = scrapy.Field()
    difficulty = scrapy.Field()
    ac_rate = scrapy.Field()
    likes = scrapy.Field()
    dislikes = scrapy.Field()
    slug = scrapy.Field()
