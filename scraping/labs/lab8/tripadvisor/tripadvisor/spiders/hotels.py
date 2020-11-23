import scrapy
from scrapy import Request
from ..items import HotelItem


class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['tripadvisor.fr']
    start_urls = ['https://www.tripadvisor.fr/Hotels-g45963-Las_Vegas_Nevada-Hotels.html']

    def parse(self, response):
        hotels = response.css('div.listItem')
        for item in hotels:
            hotel = HotelItem()

            hotel['name'] = item.css('div.listing_title a ::text').get().strip()
            hotel['review'] = float(item.css('a.ui_bubble_rating ::attr(alt)').get().split()[0].replace(',', '.')) if ' ' in item.css('a.ui_bubble_rating ::attr(alt)').get() else 0
            hotel['reviewCount'] = item.css('a.review_count ::text').get().replace(' avis', '')

            yield hotel

        next_page = response.css('a.next ::attr(href)').get()
        print(next_page)
        if next_page:
            print(response)
            next_page = response.urljoin(next_page)
            yield Request(url=next_page, callback=self.parse)


