import scrapy


class CategoriesSpider(scrapy.Spider):
    name = "categories"

    def start_requests(self):
        urls = [
            'http://www.nonetflix.com.br/categoria/acao-e-aventura'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'categories-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)