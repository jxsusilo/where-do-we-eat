from api import FoodPicker
from generator import Room


def main(): 
    location = input("Enter location: ")
    room = Room(location)

    pars = ['Annie', 'Bob', 'Chris', 'David', 'Eve']
    for p in pars: 
        room.add_particpant(p)

    prices = ['$', '$$', '$$$', '$$$$']
    results = room.result('american', prices) 


    for r in results: 
        print(r.location)
    
    