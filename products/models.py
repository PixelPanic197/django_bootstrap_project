# products/models.py
from django.db import models

class Product(models.Model):
    article = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    confirmation_date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return self.article