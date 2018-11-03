from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
import json, datetime

from orders.models import Menu_Item, Topping, Orders, OrderItems, OrderItemsToppings

shopping_cart_list = []
# Create your views here.
def index(request):
    # return HttpResponse("Project 3: TODO")
    return render(request, 'index.html')

@ensure_csrf_cookie 
def menu(request):
    # View function for Menu page

    #generate lists of menu items by category
    sandwiches = Menu_Item.objects.filter(category='sub')
    reg_pizzas = Menu_Item.objects.filter(category='pizza', subcategory="regular")
    sic_pizzas = Menu_Item.objects.filter(category='pizza', subcategory="sicilian")
    salads = Menu_Item.objects.filter(category='salad')
    pasta = Menu_Item.objects.filter(category='pasta')
    dinner_platters = Menu_Item.objects.filter(category='dinner platters')
    # toppings = Topping.objects.all()

    context = {
        'sandwiches':sandwiches,
        'reg_pizzas': reg_pizzas,
        'sic_pizzas': sic_pizzas,
        'pasta': pasta,
        'salads': salads,
        'dinner_platters':dinner_platters,
        # 'toppings': toppings,
    }
    return render(request, 'menu.html', context=context)

def shoppingcart(request):
    context={
        'shoppingcart':shopping_cart_list,
    }
    return render(request, 'shoppingcart.html',context=context)
def addtocart(request):
    if request.user.is_authenticated:
        response = JsonResponse({"foo":"bar"})
        currentUser = request.user
    print(currentUser.id, request.body)    
    orderinfo = json.loads(request.body)
    # print(orderinfo)
    menu_item = Menu_Item.objects.get(pk=int(orderinfo[0]['id']))
    orderitem = OrderItems(item=menu_item,size=orderinfo[0]['size'],price=orderinfo[0]['cost'])
    toppings = orderinfo[0]['toppings']
    print(orderitem.size,orderitem.price,orderitem.item, toppings)
    orderitem.save()
    if toppings:
        for item in toppings:
            topping_item = Topping.objects.get(pk=item['id'])
            topping = OrderItemsToppings(orderitems=orderitem,topping=topping_item,price=item['cost'])
            topping.save()
            print(item)
    shopping_cart_list.append(orderitem)
    return response
def removefromcart(request):
    print('remove from cart 1st print',request.body.decode('utf-8'))
    itemID = request.body.decode('utf-8')
    item_to_remove = OrderItems.objects.get(pk=itemID)
    shopping_cart_list.remove(item_to_remove)
    item_to_remove.delete()
    response = JsonResponse({"foo":"bar"})
    return response

def placeorder(request):
    if not request.user.is_authenticated:
        return
    user = request.user
    now = datetime.datetime.now()
    current_order = Orders(customer=user, date=now)
    current_order.save()
    for orderItem in shopping_cart_list:
        orderItem.order = current_order
        orderItem.save()
    shopping_cart_list = []
def user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request,'user.html')