from django.db import models

# Create your models here.
class Customer(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)

class Employee(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    rank = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.last}, {self.first} -- Position: {self.rank}"

class Toppings(models.Model):
    name = models.CharField(max_length=64)
    cost_LargeReg_Pizza = models.DecimalField(max_digits=6, decimal_places=2)
    cost_SmallReg_Pizza = models.DecimalField(max_digits=6, decimal_places=2)
    cost_LargeSic_Pizza = models.DecimalField(max_digits=6, decimal_places=2)
    cost_SmallSic_Pizza = models.DecimalField(max_digits=6, decimal_places=2)
    cost_Small_Sub = models.DecimalField(max_digits=6, decimal_places=2)
    cost_Large_Sub = models.DecimalField(max_digits=6, decimal_places=2)

class Menu_Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    subcategory = models.CharField(max_length=64)
    toppings = models.CharField(max_length=64)
    price_large = models.DecimalField(max_digits=6, decimal_places=2)
    price_small = models.DecimalField(max_digits=6, decimal_places=2)
