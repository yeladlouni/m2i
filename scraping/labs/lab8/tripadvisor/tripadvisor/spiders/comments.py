import scrapy


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['tripadvisor.fr']
    start_urls = ['http://tripadvisor.fr/']

    def parse(self, response):
        pass
