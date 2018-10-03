from django.core.management.base import BaseCommand
from orders.models import Menu_Item

# f = open("items.txt", "r")
# print('test')
# for line in f:
#     print(line)
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

data_list = []
class Command(BaseCommand):
    def handle(self, **options):
        f = open("subs.txt", "r")
        print('test')
        for line in f:
            if line[-1] == "\n":
                line = line[0:-1]
            x = line.split("\t")
            name = x[0].strip()
            # print(x,x[0].strip(),x[1],x[2])
            # priceSmall = float(x[1])
            # priceBig = float(x[2])
            priceSmall = (float(x[1]) if isfloat(x[1]) else None)
            priceBig = (float(x[2]) if isfloat(x[2]) else None)
            data_list.append([name, priceSmall,priceBig])

            newMenuItem = Menu_Item(name=name,price_small=priceSmall,price_large=priceBig,
                    category="sub",toppings="cheese")
            newMenuItem.save()
        for menuItem in data_list:
            print(menuItem)
