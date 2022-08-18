from django.db import models
from main.models import Product

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    address = models.IntegerField()
    full_price = models.IntegerField()
    

class OrderedProducts (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    