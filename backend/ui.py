import sys
import os

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
            

def main(): 
    location = input("Enter location: ")
    room_code = input("Enter code, or one will be generated (press enter): ")
    if len(room_code) == 0: 
        room_code = code()
        new_session = Room(location, room_code)
        rooms[room_code] = new_session
    
    room1 = rooms[room_code]
    #prices = ['$', '$$', '$$$', '$$$$']
    prices = ['$$$$']
    room1.result('american', prices) 

    while True: 
        room1.show_restaurant_list()
        option = input('Enter D/U and integer option to vote: \n')
        if len(option) == 0:
            return 
        else: 
            letter = option[0].strip()
            number = int(option[1:].strip())
            if letter.upper() == 'D': 
                room1.vote(number, -1)
            elif letter.upper() == 'U': 
                room1.vote(number, 1)
        
        print(room1._cuisines.items())
    