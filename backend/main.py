from multiprocessing import cpu_count
from traceback import print_exception
from pcpartpicker import API 
from decimal import Decimal
import csv


api = API()

class Component:
    def __init__(self, part, price, region='ca'):
        self.api = API(region)
        self.supported_parts = api.supported_parts
        self.part = part 
        self.items = self.api.retrieve(part)
        self.price = price
        
        


    def get_component_json(self, component: str):
        return self.items

    def get_items_p(self):
        ''' Get items from price range '''
        upper = self.price * 1.25
        lower = self.price * 0.75
    
        comps = []
        for item in self.items[self.part]:
           if item.price.amount <= Decimal(upper) and item.price.amount >= Decimal(lower):
                if len(comps) < 5:
                    comps.append(item)
                else:
                    break
        return comps

    
        


cpu = Component('motherboard', 200)


#print(cpu.supported_parts)
#get components based on component price ratio 
 
ratio = {'motherboard': 0.15, 'cpu': 0.15, 'video-card': 0.50, 'memory': 0.10}

parts_list = {}

def get_parts(price):
    for key in ratio:
        print(key)
        part = Component(key, price*ratio[key])
        parts_list[key] = part.get_items_p()

get_parts(2000)

f = open("out.txt", "w")
f.writelines(parts_list)
f.close()
