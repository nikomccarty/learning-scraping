# Tutorial from https://www.youtube.com/watch?v=s4jtkzHhLzY

import scrapy

class WhiskySpider(scrapy.Spider):
    name = "whisky"
    start_urls = [
        'https://www.whiskyshop.com/scotch-whisky/all?price=0-100500'
    ]

    def parse(self, response):
        for product in response.css("div.product-item-info"):
            try:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': product.css('span.price::text').replace('£', ''),
                    'link': product.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': product.css('a.product-item-link').attrib['href'],
                }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)