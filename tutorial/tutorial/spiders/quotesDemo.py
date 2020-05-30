import scrapy
from scrapy.http import FormRequest
from ..items import TutorialItem
from scrapy.utils.response import open_in_browser


class QuotesScrappingExample(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/login',
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'test@gmail.com',
            'password': 'asdasd'
        }, callback=self.login)

    def login(self, response):
        open_in_browser(response)
        items = TutorialItem()
        all_quotes = response.css("div.quote")
        for quote in all_quotes:
            title = quote.css("span.text::text").extract()
            author_name = quote.css(".author::text").extract()
            all_tags = quote.css(".tag::text").extract()

            items['title'] = title
            items['author_name'] = author_name
            items['all_tags'] = all_tags

            yield items
        next_items = "http://quotes.toscrape.com/page/" + str(QuotesScrappingExample.page_number) + "/"

        if QuotesScrappingExample.page_number < 11:
            QuotesScrappingExample.page_number += 1
            yield response.follow(next_items, callback=self.parse)
