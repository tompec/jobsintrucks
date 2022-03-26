import scrapy
from scrapy.linkextractors import LinkExtractor

class MySpider(scrapy.Spider):
    name = "myspider"

    allowed_domains = ['www.jobsintrucks.com']
    start_urls = [
        'https://www.jobsintrucks.com/',
    ]

    def parse(self, response):

        le = LinkExtractor()
        links = le.extract_links(response)

        for link in links:
            yield response.follow(link.url, callback=self.parse)

        data = {
            'url': response.url,
            'title': response.xpath('string(//title)').extract_first(),
            'description': response.xpath('string(//meta[@name="description"]/@content)').extract_first(),
            'html': response.text,
        }

        yield data
