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
            if link[:22] != 'https://www.google.com':
                link = 'https://' + self.allowed_domains[0] + link 

            yield {"tipo": "busca", "produto": text, 'link': link, 'ean': self.ean}


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
        title = response.xpath('//h1[@id="product-name"]/text()').extract()
        url_lojas = response.xpath('//a[contains(@class, \'pag-detail-link\')]/@href').getall()
        url_imagem = response.xpath('//img[contains(@class, \'TL92Hc\')]/@src').extract_first()

        if url_lojas[0][:22] != 'https://www.google.com':
                url_lojas[0] = 'https://' + self.allowed_domains[0] + url_lojas[0]

        yield {"tipo": "produto", "title": title, "url_imagem": url_imagem, "url_lojas": url_lojas[0], "ean": self.ean, 'url': self.url}


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

        a_selectors = response.xpath('//*[contains(@class, \'os-row\')]/h3/a')
        for selector in a_selectors:
            seller = ''.join(selector.xpath("//*[contains(@class, \'os-seller-name-primary\')]/text()").extract()).strip()
            payment = ''.join(selector.xpath("//*[contains(@class, \'os-details-col\')]/text()").extract()).strip()
            total = ''.join(selector.xpath("//*[contains(@class, \'os-price-col\')]/text()").extract()).strip()  # os-price-col
            payment = payment.split("x")


            yield {"tipo": "loja", "product": text, 'link': self.allowed_domains[0] + link, 'parcela': payment[0], 'valor_parcela': payment[1], 'total':total, 'id': self.id}



