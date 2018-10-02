from django.core.management.base import BaseCommand
from orders.models import Topping

# f = open("items.txt", "r")
# print('test')
# for line in f:
#     print(line)
data_list = []
class Command(BaseCommand):
    def handle(self, **options):
        f = open("items.txt", "r")
        print('test')
        for line in f:
            if line[-1] == "\n":
                line = line[0:-1]
            print(line)
            data_list.append(line)

        print(data_list)
