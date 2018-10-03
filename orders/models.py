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

class Topping(models.Model):
    name = models.CharField(max_length=64)
    cost_LargeReg_Pizza = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_SmallReg_Pizza = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_LargeSic_Pizza = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_SmallSic_Pizza = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_Small_Sub = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cost_Large_Sub = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=128)


    def __str__(self):
        return (f"{self.id} {self.name} Small Reg:{self.cost_SmallReg_Pizza} Large Reg: {self.cost_LargeReg_Pizza} Small Sic: {self.cost_SmallSic_Pizza} "
                f"Large Sic: {self.cost_LargeSic_Pizza} Small Sub: {self.cost_Small_Sub} Large Sub: {self.cost_Large_Sub}")



class Menu_Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64, null=True, blank=True)
    subcategory = models.CharField(max_length=64, null=True, blank=True)
    toppings = models.CharField(max_length=64, null=True, blank=True)
    price_large = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_small = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    included_toppings = models.IntegerField(null=True, blank=True)
