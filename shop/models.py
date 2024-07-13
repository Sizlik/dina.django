from django.db import models

from core.models import BaseModel


class Shop(BaseModel):
    class Type(models.TextChoices):
        PRODUCT = 'product'
        SERVICE = 'service'
        TECH = 'tech'

    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, max_length=100)
    type = models.CharField(choices=Type.choices, default=Type.PRODUCT, max_length=20)


class ShopItem(BaseModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


