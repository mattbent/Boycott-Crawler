import scrapy

class BoycottSpider(scrapy.Spider):
	name = "articles"

	def start_requests(self):
		urls=[
			'https://www.nytimes.com'
			'http://www.latimes.com/'
			'http://www.chicagotribune.com/'
			'http://www.wsj.com/'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f: f.write(response.body)
        self.log('Saved file %s' % filename)
