from django.db import models


# Create your models here.

class IPInfo(models.Model):
    status = models.CharField(verbose_name="Status", max_length=20, default="success")
    ip = models.CharField(verbose_name='Ip', max_length=128, db_index=True)
    int_prov = models.CharField(verbose_name='Int_prov', max_length=100)
    org = models.CharField(verbose_name='Org', max_length=100)
    country = models.CharField(verbose_name='Country', max_length=100)
    region_name = models.CharField(verbose_name='Region name', max_length=100)
    city = models.CharField(verbose_name='City', max_length=100)
    zip = models.CharField(verbose_name='ZIP', max_length=20)
    lat = models.FloatField(verbose_name='Lat')
    lon = models.FloatField(verbose_name='Lon')


# class InvalidData:
#     status = 'fail'
#     message = ''
#     query = ''
#
#     def __init__(self, status, message, query):
#         self.status = status
#         self.message = message
#         self.query = query
