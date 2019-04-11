# -*- coding: utf-8 -*-
import scrapy


class FirstspiderSpider(scrapy.Spider):
    name = 'firstspider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
