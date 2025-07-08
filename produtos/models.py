from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(100)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    unit = models.CharField(max_length=150)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    observed_on = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
