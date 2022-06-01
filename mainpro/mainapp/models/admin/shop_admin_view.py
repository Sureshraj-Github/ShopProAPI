from django.db import models

class ShopAdminView(models.Model):
    date = models.CharField(max_length=100, null=True, blank=True)
    store_name = models.CharField(max_length=100, null=True, blank=True)
    # image=models.ImageField(upload_to='images/')
    store_km = models.CharField(max_length=100, null=True, blank=True)
    store_item = models.CharField(max_length=100, null=True, blank=True)
    store_min_order = models.CharField(max_length=100, null=True, blank=True)