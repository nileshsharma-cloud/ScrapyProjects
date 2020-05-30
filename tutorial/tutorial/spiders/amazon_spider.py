import scrapy
from scrapy.http import FormRequest
from ..items import TutorialItem
from scrapy.utils.response import open_in_browser
from ..items import Amazon

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/s?k=books&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        books = Amazon()
        title = response.css(".a-size-medium::text").extract()
        price = response.css(".a-spacing-top-small .a-price-whole::text").extract()
        author = response.css(".sg-col-12-of-28 .a-size-base+ .a-size-base::text").extract()




