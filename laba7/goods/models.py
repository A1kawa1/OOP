from django.db import models
from django.core.validators import MinValueValidator


class Good(models.Model):

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
