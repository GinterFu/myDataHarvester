import scrapy


class UdemyApiSpider(scrapy.Spider):
    name = "udemy_api"
    allowed_domains = ["udemy.com"]
    start_urls = ["https://udemy.com"]

    def parse(self, response):
        pass
