from itertools import product
from operator import mod
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models


class Product(models.Model):
    title = models.TextField(max_length=255)
    unit_price = models.FloatField()
    description = models.TextField(max_length=255)
    date_updated = models.DateTimeField(auto_now=True)
