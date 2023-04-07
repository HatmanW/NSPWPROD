from django.db import models
from shop.models import Order

class Cart(models.Model):
    item_name = models.CharField(max_length=30)
    item_size = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    item_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)


