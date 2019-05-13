from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import task
from threading import Thread
import os
import scrapy


from crawler_scrapy.crawler_scrapy import spiders, settings
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from pprint import pprint

from scrapy.crawler import Crawler
from .spiders import MySpider
from twisted.internet import reactor
from billiard import Process


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('tasks', broker=os.environ['CELERY_BROKER'])

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))


@task()
def pesquisa_google(ean):
    MySpider = spiders.GoogleMarketplaceSpider()
    # print(get_project_settings())
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider, ean=ean)  ## <-------------- (1)
    Thread(target=process.start).start()
    # print(ean)

@task()
def pesquisa_produto(url, ean):
    MySpider = spiders.google_marketplace.ProdutoMPSpider()
    # print(get_project_settings())
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider, url=url, ean=ean)  ## <-------------- (1)
    Thread(target=process.start).start()
    # print(ean)

@task()
def pesquisa_lojas(url, id):
    MySpider = spiders.google_marketplace.LojasMPSpider()
    # print(get_project_settings())
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider, url=url, id=id)  ## <-------------- (1)
    Thread(target=process.start).start()
    # print(ean)
