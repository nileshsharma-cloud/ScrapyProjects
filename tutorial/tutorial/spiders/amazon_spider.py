import scrapy
from ..items import Amazon


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/s?k=books&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        books = Amazon()
        book_title = response.css(".a-size-medium::text").extract()
        book_price = response.css(".a-spacing-top-small .a-price-whole::text").extract()
        book_author = response.css(".sg-col-12-of-28 .a-size-base+ .a-size-base::text").extract()
        books['book_title'] = book_title
        books['book_price'] = book_price
        books['book_author'] = book_author
        yield books





