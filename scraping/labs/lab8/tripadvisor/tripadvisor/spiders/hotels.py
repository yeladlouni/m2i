from scrapy.spiders import CrawlSpider
from scrapy import Request

class HotelsSpider(CrawlSpider):
    name = 'hotels'
    allowed_domains = ['tripadvisor.fr']
    start_urls = ['https://www.tripadvisor.fr/Hotels-g45963-Las_Vegas_Nevada-Hotels.html']

    def parse_items(self, response):
        hotels = response.css('div.listItem')
        for item in hotels:
            hotel = HotelItem()

            hotel['name'] = item.css('div.listing_title a ::text').get()
            hotel['review'] = item.css('a.ui_bubble_rating ::attr(alt)').get()
            hotel['reviewCount'] = item.css('a.review_count ::text').get()

            next_page = response.css('a.next ::attr(href)').get()

            if next_page:
                print(response)
                next_page = response.urljoin(next_page)
                yield Request(url=next_page, callback=self.parse)

            return hotel