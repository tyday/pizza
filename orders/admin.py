from django.contrib import admin

from .models import Customer, Employee,Topping,Menu_Item

# Register your models here.

class EmployeeInline(admin.ModelAdmin):
    list_display = ('id', 'last', 'first', 'email', 'rank')
    list_editable = ('last', 'first', 'email', 'rank')

# class CustomerInline(admin.StackedInline):
#     model = Customer
#     extra = 1

admin.site.register(Customer)
admin.site.register(Employee, EmployeeInline)
admin.site.register(Topping)
admin.site.register(Menu_Item)