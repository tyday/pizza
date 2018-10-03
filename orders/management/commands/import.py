from django.core.management.base import BaseCommand
from orders.models import Topping

# f = open("items.txt", "r")
# print('test')
# for line in f:
#     print(line)
# data_list = []
class Command(BaseCommand):
    def handle(self, **options):
        f = open("items.txt", "r")
        print('test')
        for line in f:
            if line[-1] == "\n":
                line = line[0:-1]
            # print(line)
            # data_list.append(line)
            newTopping = Topping(name=line,cost_LargeReg_Pizza=2.00, cost_SmallReg_Pizza=1.00,
                cost_LargeSic_Pizza=2.00, cost_SmallSic_Pizza=1.00)
            newTopping.save()


        # print(data_list)
