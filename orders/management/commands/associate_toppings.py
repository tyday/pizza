from django.core.management.base import BaseCommand
from orders.models import Menu_Item, Topping

class Command(BaseCommand):
    def handle(self, **options):
        for menuItem in Menu_Item.objects.all():
            # menuItem.description = "This is a description of the menu item"
            # menuItem.save()
            try:
                for topping in Topping.objects.filter(category__contains = menuItem.toppings):
                    menuItem.allowed_toppings.add(topping)
                    # print(f'partially succeeded with {menuItem.name}')
                menuItem.save()
            except:
                print(f'failed with {menuItem.name}')