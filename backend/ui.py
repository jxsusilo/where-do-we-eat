import sys
import os
import math

# Add the project root directory to the Python path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from backend.generator import Room, rooms
import random 
import string

def code() -> str: 
    '''Returns a room code of length max_len'''
    MAX_LEN = 6
    while True: 
        res = ''.join(random.choices(string.ascii_uppercase +
                string.digits, k=MAX_LEN))
        if not(res in rooms.keys()):
            return str(res)
        
def logistics(): 
    location = input("Enter location: ")
    room_code = input("Enter code, or one will be generated (press enter): ")
    if len(room_code) == 0: 
        room_code = code()
        new_session = Room(location, room_code)
        rooms[room_code] = new_session
    room1 = rooms[room_code]
    return room1
            
def prices(): 
    price = ['$', '$$', '$$$', '$$$$']
    maximum = int(input('Up to how many dollar signs would you like? (1-4): '))
    return price[:maximum-1]

def ask_cuisine(room: Room): 
    total = set()
    while True: 
        cuisine = input('What cuisine would you like? ')
        if len(cuisine) == 0: 
            return total 
        else: 
            total.add(cuisine)
        room.vote_cuisine(cuisine)

def voting(room: Room): 
    room.show_restaurant_list()
    option = input('Enter D/U and integer option to vote: \n')
    if len(option) == 0:
        return 
    else: 
        letter = option[0].strip()
        number = int(option[1:].strip())
        if letter.upper() == 'D': 
            room.vote(number, -1)
        elif letter.upper() == 'U': 
            room.vote(number, 1)

def main(): 
    room1 = logistics()
    price = prices()
    all_cuisines = ask_cuisine(room1)
    while True: 
        room1.give_final_results(all_cuisines, price)
        voting(room1)