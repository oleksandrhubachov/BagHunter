from scrapy import Selector
from scrapy.contrib.spiders.crawl import CrawlSpider


class BagHunterSpider(CrawlSpider):
    name = "hunter"
    allowed_domains = ['511tactical.com']
    start_urls = ['http://www.511tactical.com/covrt-18-backpack.html']
    xpath = '//*[@id="product-price-41861"]/span/text()'

    def parse_start_url(self, response):
        hxs = Selector(response)
        result = hxs.xpath(self.xpath).extract()[0]
        print result