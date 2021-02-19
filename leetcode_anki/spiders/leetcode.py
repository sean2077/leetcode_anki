import scrapy


class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    allowed_domains = ['https://leetcode.com']
    start_urls = ['http://https://leetcode.com/']

    def parse(self, response):
        pass
