from asyncio.windows_events import NULL
from operator import truediv
from statistics import mode
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.TextField(max_length=50)
    def __str__(self):
        return self.title

class Promotion(models.Model):
    title= models.TextField(max_length=50)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.TextField(max_length=50)
    unit_price = models.FloatField()
    description = models.TextField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(null=True, blank=True)
    code = models.TextField(max_length=15, null=True, default="N/A", blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.title
    



