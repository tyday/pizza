from django.core.management.base import BaseCommand
from orders.models import Menu_Item

class Command(BaseCommand):
    def handle(self, **options):
        for menuItem in Menu_Item.objects.all():
            menuItem.description = "This is a description of the menu item"
            menuItem.save()