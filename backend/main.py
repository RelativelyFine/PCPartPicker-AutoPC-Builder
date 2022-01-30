from multiprocessing import cpu_count
from pcpartpicker import API 
from decimal import Decimal


api = API()

class Components:
    def __init__(self, part, region='ca'):
        self.api = API(region)
        self.supported_parts = api.supported_parts
        self.part = part 
        self.items = self.api.retrieve(part)
        
        


    def get_component_json(self, component: str):
        return self.items

    def get_items_p(self, lower, upper):
        ''' Get items from price '''
        comps = []
        for item in self.items[self.part]:
           if item.price.amount <= Decimal(upper) and item.price.amount >= Decimal(lower):
                if len(comps) < 5:
                    comps.append(item)
                else:
                    break
        return comps

    
        


cpu = Components('motherboard')

print(cpu.get_items_p(500, 900))