from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model) :
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=30, blank=True) 
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address= models.CharField(max_length=300, blank=True)
    total = models.DecimalField(max_digits=7 , decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class OrderDetail (models.Model) :
    product = models.CharField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=7 , decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def sub_total (self):
        return self.price * self.quantity