from django.db import models
import datetime


# Create your models here.
class MarketplaceGoogle(models.Model):
    id = models.AutoField(primary_key=True)
    ean = models.CharField(max_length=14)
    data = models.DateField(default=datetime.date.today(), blank=False)
    hora = models.TimeField(default=datetime.datetime.now().time(), blank=False)
    status = models.CharField(max_length=1, default='S')
    url = models.TextField(blank=True)
    imagem = models.TextField(blank=True)

    class Meta:
        app_label = 'MarketplaceGoogle'
        db_table = 'marketplace_google'

class PrecoMarketplaceGoogle(models.Model):
    id = models.IntegerField()
    preco = models.FloatField()
    parcela = models.IntegerField()
    valor_parcela = models.FloatField()
    taxa_juros = models.CharField(max_length=45)
    vendedor = models.TextField(blank=True, max_length=255)
    imagem = models.TextField(blank=True)

    class Meta:
        app_label = 'PrecoMarketplaceGoogle'
        db_table = 'preco_marketplace_google'



