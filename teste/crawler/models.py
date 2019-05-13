from django.db import models
import datetime


# Create your models here.
class MarketplaceGoogle(models.Model):
    id = models.IntegerField(primary_key=True)
    ean = models.CharField(max_length=14)
    data = models.DateField(default=datetime.date.today(), blank=False)
    hora = models.TimeField(default=datetime.datetime.now().time(), blank=False)
    status = models.BooleanField()
    url = models.TextField(blank=True)
    imagem = models.TextField(blank=True)

    class Meta:
        app_label = 'MarketplaceGoogle'
        db_table = 'marketplace_google'