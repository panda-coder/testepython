# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlparse


class GoogleMarketplaceSpider(scrapy.Spider):
    name = 'google_marketplace'
    allowed_domains = ['www.google.com']
    # start_url = 'https://www.google.com/search?tbm=shop&hl=pt-BR&source=hp&biw=&bih=&q=%s&oq=%s'
    start_url = 'https://www.google.com/search?tbm=shop&hl=pt-BR&source=hp&biw=&bih=&q=%s&oq=%s'

    def __init__(self, ean=None):
        self.ean = ean

    def start_requests(self):
        if self.ean:  # taking input from command line parameters
            url = self.start_url % (self.ean, self.ean)
            yield self.make_requests_from_url(url)

    def parse(self, response):

        a_selectors = response.xpath('//*[contains(@class, \'MCpGKc\')]/h3/a')
        for selector in a_selectors:
            text = ''.join(selector.xpath("text()").extract()).strip()
            link =  selector.xpath("@href").extract_first()
            yield {"tipo": "busca", "product": text, 'link': 'https://' + self.allowed_domains[0] + link, 'ean': self.ean}


class ProdutoMPSpider(scrapy.Spider):
    name = 'google_marketplace'
    allowed_domains = ['www.google.com']

    def __init__(self, url=None, ean=None):
        self.url = url
        self.ean = ean

    def start_requests(self):
        if self.url:  # taking input from command line parameters
            url = self.url
            yield self.make_requests_from_url(url)

    def parse(self, response):
        print(response.body)
        title = response.xpath('//h1[@id="product-name"]/text()').extract()
        url_lojas = response.xpath('//a[contains(@class, \'pag-detail-link\')]/@href').getall()
        url_imagem = response.xpath('//img[contains(@class, \'TL92Hc\')]/@src').extract_first()

        yield {"tipo": "loja", "title": title, "url_image": url_imagem, "url_lojas": url_lojas[0], "ean": self.ean}

        # a_selectors = response.xpath('//*[contains(@class, \'MCpGKc\')]/h3/a')
        # for selector in a_selectors:
        #     text = ''.join(selector.xpath("text()").extract()).strip()
        #     link =  selector.xpath("@href").extract_first()
        #     yield {"tipo": "produto", "product": text, 'link': 'https://' + self.allowed_domains[0] + link}


class LojasMPSpider(scrapy.Spider):
    name = 'google_marketplace'
    allowed_domains = ['www.google.com']

    def __init__(self, url=None, id=None):
        self.url = url
        self.id = id

    def start_requests(self):
        if self.url:  # taking input from command line parameters
            url = self.url
            yield self.make_requests_from_url(url)

    def parse(self, response):

        a_selectors = response.xpath('//*[contains(@class, \'MCpGKc\')]/h3/a')
        for selector in a_selectors:
            text = ''.join(selector.xpath("text()").extract()).strip()
            link =  selector.xpath("@href").extract_first()
            yield {"tipo": "loja", "product": text, 'link': self.allowed_domains[0] + link}



