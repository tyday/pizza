from django.db import models
# these are to extend the user model
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.http import JsonResponse
import json



# Create your models here.

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
    def __repr__(self):
        return (f"{self.id}")

class Menu_Item(models.Model):
    """Individual Item (pizza/sandwich)

    Attributes:
        name            name of item
        category        
        subcategory
        toppings        category reference to Toppings.category
        price_large     cost for large size
        price_small     cost for small
        included_toppings   integer that holds number of toppings included at cost
        description     description
        allowedtoppings     not exactly sure what this does
    """
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64, null=True, blank=True)
    subcategory = models.CharField(max_length=64, null=True, blank=True)
    toppings = models.CharField(max_length=64, null=True, blank=True)
    price_large = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_small = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    included_toppings = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    allowedtoppings = models.ManyToManyField(Topping)

    def getInvoiceName(self):
        returnList = []
        if self.subcategory:
            returnList.append(self.subcategory)
        if self.category:
            returnList.append(self.category)
        if self.name:
            returnList.append(self.name)
        return str.title(" ".join(returnList))
    def getItemJson(self):
        returnDict = {}
        id = self.id
        name = self.name
        price_large = str(self.price_large)
        price_small = str(self. price_small)
        invoice_name = self.getInvoiceName()
        returnDict = {"id":id, "name":name,"price_large":price_large,"price_small":price_small,"invoice_name":invoice_name}
        return json.dumps(returnDict)

    def getToppings(self):
        returnDict = {}
        for item in self.allowedtoppings.all():
            itemname = item.name
            if self.category == 'pizza' and self.subcategory == 'sicilian':
                price = {'price_large':str(item.cost_LargeSic_Pizza),'price_small':str(item.cost_SmallSic_Pizza)}
            elif self.category == 'pizza' and self.subcategory == 'regular':
                price = {'price_large':str(item.cost_LargeReg_Pizza),'price_small':str(item.cost_SmallReg_Pizza)}
            elif self.category == 'sub':
                price = { "price_large":str(item.cost_Large_Sub),"price_small":str(item.cost_Small_Sub)}
            else:
                price = {}
            price["id"] = item.id
            returnDict[itemname] = price
        return json.dumps(returnDict)

class Orders(models.Model):
    """Holds OrderItems

    Attributes:
        customer    A user
        date        a datetime.datetime
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
class OrderItems(models.Model):
    """An individual item (A pizza, a sandwich)
        holds OrderItemsToppings
    
    Attributes:
        order   a class Order reference
        item    a class Menu_Item reference
        size    a string (large/small)
        price   a decimal field

        total_cost  returns cost of item and toppings
    """
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Menu_Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def total_cost(self):
        ret_total_cost = 0.00
        ret_total_cost += float(self.price)
        for topp in self.orderitemstoppings_set.all():
            ret_total_cost += float(topp.price)
        return ret_total_cost
class OrderItemsToppings(models.Model):
    orderitems = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=10,null=True,blank=True)
    address = models.TextField(max_length=250,null=True,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()