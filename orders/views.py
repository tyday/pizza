from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from orders.models import Menu_Item


# Create your views here.
def index(request):
    # return HttpResponse("Project 3: TODO")
    return render(request, 'index.html')

def menu(request):
    # View function for Menu page

    #generate lists of menu items by category
    sandwiches = Menu_Item.objects.filter(category='sub')
    reg_pizzas = Menu_Item.objects.filter(category='pizza', subcategory="regular")
    sic_pizzas = Menu_Item.objects.filter(category='pizza', subcategory="sicilian")
    salads = Menu_Item.objects.filter(category='salad')

    context = {
        'sandwiches':sandwiches,
        'reg_pizzas': reg_pizzas,
        'sic_pizzas': sic_pizzas,
        'salads': salads,
    }
    return render(request, 'menu.html', context=context)

def user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request,'user.html')