import scrapy


class YellowPagesSpider(scrapy.Spider):
    name = 'yellowpages'
    start_urls = ['https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=pharmacie&ou=Paris']

    def parse(self, response):
        companies = response.css(' div.zone-bi > header ')
        for company in companies:
            company_name = company.css('div.row-denom > div.denomination.with-stars > h3 > a ::text').get()
            company_address = company.css('div.main-adresse-container.row-adresse.with-adresse.with-horaire-chaudes > div.adresse-container.noTrad > a ::text').get

            yield {'name': company_name.replace_all('"', '')}

