import json
import logging
import os
import re

import requests
from leetcode_anki.items import QuestionDataItem
from leetcode_anki.login import login
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from scrapy.loader.processors import SelectJmes
from scrapy.shell import inspect_response


class LeetcodeSpider(scrapy.Spider):
    session: requests.Session

    name = "leetcode"
    allowed_domains = ["leetcode.com"]

    def start_requests(self):
        self.session = login()
        questionset_url = "https://leetcode.com/api/problems/all/"
        yield scrapy.Request(url=questionset_url, callback=self.parse_question_set)

    def parse_question_set(self, response: HtmlResponse):
        self.logger.info(type(response))
        jsonresponse = json.loads(response.text)
        print(json.dumps(jsonresponse, indent=4))
        # loader = ItemLoader(item=QuestionDataItem())

        question_url = "https://leetcode.com/graphql"
        question_set = jsonresponse["stat_status_pairs"]
        for question in question_set:
            title_slug = question["stat"]["question__title_slug"]

    def parse_question_data(self, response: HtmlResponse):
        pass

    def get_submission_list(self, slug):
        pass

    def handle_code(self, code):
        code = code.replace("\\u0009", "\t")
        code = code.replace("\\u000A", "\n")
        code = code.replace("\\u0027", "'")
        code = code.replace("\\u0022", '"')
        code = code.replace("\\u002D", "-")
        code = code.replace("\\u003C", "<")
        code = code.replace("\\u003E", ">")
        code = code.replace("\\u003D", "=")
        code = code.replace("\\u003B", ";")
        code = code.replace("\\u0026", "&")
        code = code.replace("\\u002A", "*")

        return code
