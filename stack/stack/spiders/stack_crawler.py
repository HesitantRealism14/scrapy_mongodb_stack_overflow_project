import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from stack.items import StackItem

class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    rules = [Rule(LinkExtractor(allow=r'\\questions/\?page=[0-9]&sort=newest'),callback='parse_item', follow=True)]

    def parse_item(self, response):
        questions = Selector(response).xpath('//div[@id="questions"]')

        for question in questions:
            item = StackItem()
            item['url'] = question.xpath(
                '//h3[@class="s-post-summary--content-title"]/a/text()').extract()
            item['title'] = question.xpath(
                '//h3[@class="s-post-summary--content-title"]/a/@href').extract()
            yield item
