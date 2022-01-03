from django.db import models

from apps.utils.models import TimeStamps


class Product(TimeStamps):
    name = models.CharField(max_length=256,unique=True)
    price = models.FloatField()
    discount = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} : {self.price}"
