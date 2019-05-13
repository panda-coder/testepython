# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawler import tasks
from crawler import models


class CrawlerScrapyPipeline(object):
    @staticmethod
    def process_item(item, spider):
        if item['tipo'] == "busca":
            print("aqui... busca")
            tasks.pesquisa_produto.delay(item['link'], item['ean'])
        elif item['tipo'] == "produto":
            mp_google = models.MarketplaceGoogle(ean=item['ean'], status='S', imagem=item['url_imagem'], url=item['url'])
            mp_google.save()

            tasks.pesquisa_lojas.delay(item['url_lojas'], mp_google.id)

        elif item['tipo'] == "loja":
            print("***********************************************************")
            mp_google = models.PrecoMarketplaceGoogle(id=item['id'] )
            mp_google.save()
            print("***********************************************************")

        return item
