import scrapy


class WorldSpider(scrapy.Spider):
    name = "world"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        rows = response.css('table.datatable tbody tr')

        for row in rows:
            yield {
                'country': row.css('td:nth-child(2) a::text').get(),
                'population': row.css('td:nth-child(3)::text').get(),
                'land_area': row.css('td:nth-child(7)::text').get(),
                'link': response.urljoin(row.css('td:nth-child(2) a::attr(href)').get())
            }
