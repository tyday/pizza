from django.contrib import admin

from .models import Topping,Menu_Item

# Register your models here.

class ToppingInline(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost_SmallReg_Pizza','cost_LargeReg_Pizza',
                    'cost_SmallSic_Pizza','cost_LargeSic_Pizza','cost_Small_Sub','cost_Large_Sub', 'category')
    list_editable = ('name', 'cost_SmallReg_Pizza','cost_LargeReg_Pizza',
                    'cost_SmallSic_Pizza','cost_LargeSic_Pizza','cost_Small_Sub','cost_Large_Sub', 'category')
class Menu_ItemInline(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'subcategory','price_small','price_large',
                    'toppings','included_toppings')
    list_editable = ('name', 'category', 'subcategory','price_small','price_large',
                    'toppings','included_toppings')


admin.site.register(Topping, ToppingInline)
admin.site.register(Menu_Item, Menu_ItemInline)