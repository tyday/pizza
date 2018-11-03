from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("user/", views.user, name="user"),
    path("shoppingcart/", views.shoppingcart, name="shoppingcart"),
    path("addtocart/", views.addtocart, name="addtocart"),
    path("removefromcart/", views.removefromcart, name="removefromcart"),
    path("placeorder/", views.placeorder,name="placeorder"),
]
