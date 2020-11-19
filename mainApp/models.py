from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField()
    brand = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"