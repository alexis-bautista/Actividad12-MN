import scrapy


class TitularesSpider(scrapy.Spider):
    name = "titulares"
    start_urls = ["https://www.bbc.com/news"]

    def parse(self, response):
        # Selecciona los elementos que contienen los titulares
        for article in response.css("div.gs-c-promo"):
            yield {
                "title": article.css("h2::text").get(),  # Extrae el texto del titular.
            }
