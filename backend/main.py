from multiprocessing import cpu_count
from traceback import print_exception
from pcpartpicker import API 
import random
from decimal import Decimal
import csv
import json

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
        for item in (self.items[self.part]):
           if item.price.amount <= Decimal(upper) and item.price.amount >= Decimal(lower):
                print(item.brand)
                if (len(comps) < 10):
                    comps.append(str(item.brand)+', '+str(item.model)+', '+str(item.price))
                else:
                    break
        return comps

def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
     data = {}
        
        # Open a csv reader called DictReader
     with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
            
            # Convert each row into a dictionary
            # and add it to data
        for rows in csvReader:
                
                # Assuming a column named 'No' to
                # be the primary key
            key = rows['component']
            data[key] = rows
    
        # Open a json writer, and use the json.dumps()
        # function to dump data
     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    
        
cpu = Component('cpu', 200)


#get components based on component price ratio 
f = open("cpu.txt", 'w')
f.write(str(cpu.items))
f.close()

ratio = {'motherboard': 0.15, 'cpu': 0.15, 'video-card': 0.50, 'memory': 0.10, 'cpu-cooler': 0.05, 'power-supply': 0.05, 'wireless-network-card': 0.01}

parts_list = {}

def get_parts(price):
    for key in ratio:
        print(key)
        part = Component(key, price*ratio[key])
        parts_list[key] = part.get_items_p()

get_parts(2000)

with open('dict.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow(['component', 'items'])
    for key, value in parts_list.items():
       writer.writerow([key, value])

csvFilePath = r'dict.csv'
jsonFilePath = r'dict.json'
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)