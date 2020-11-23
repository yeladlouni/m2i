import scrapy


class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['tripadvisor.fr']
    start_urls = ['https://www.tripadvisor.fr/Hotels-g45963-Las_Vegas_Nevada-Hotels.html']

    # taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0 > div > div:nth-child(3) > div > div.meta_listing.ui_columns.large_thumbnail_mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div.main-cols > div.comm-col > div > div > div.premium_offer_container > div > div.priceBlock.ui_column.is-12-tablet > div.price-wrap > div
    # taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0 > div > div:nth-child(3) > div > div.meta_listing.ui_columns.large_thumbnail_mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div.prw_rup.prw_meta_hsx_listing_name.listing-title > div
    def parse(self, response):
        hotels = response.css('listItem')

        for hotel in hotels:
            hotel_name = hotel.css('div.listing_title > a ::text').get()
            hotel_price = hotel.css('div.price ::text').get()
            hotel_review = hotel.css('a.ui_bubble_rating ::alt').get()
            print(hotel_name, hotel_price, hotel_review)
            #hotel_price = hotels.css('')