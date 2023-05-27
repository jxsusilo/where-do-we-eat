from api import FoodPicker
from generator import Room

"""
def main():
    key = input("Enter key, or nothing if desired: ")
    if key: 
        location = input("Enter location: ")
        cuisine = input("Enter cuisine: ")

        p = FoodPicker(location, cuisine)
        p.set_api_key(key)
    else: 
        p = FoodPicker()
    
    print(p.result())
"""

def main(): 
    location = input("Enter location: ")
    room = Room(location)

    pars = ['Annie', 'Bob', 'Chris', 'David', 'Eve']
    for p in pars: 
        room.add_particpant(p)

    a = room.result('italian') 
    for item in a: 
        print(item)