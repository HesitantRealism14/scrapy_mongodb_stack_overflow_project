from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]
    def parse(self, response):
        questions = Selector(response).xpath('//div[@id="questions"]')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                '//h3[@class="s-post-summary--content-title"]/a/text()').extract()
            item['url'] = question.xpath(
                '//h3[@class="s-post-summary--content-title"]/a/@href').extract()
            yield item
