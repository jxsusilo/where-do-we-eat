from generator import Room, rooms
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
    
    room = rooms[room_code]
    prices = ['$', '$$', '$$$', '$$$$']
    results = room.result('american', prices) 
    for r in results: 
        print(r.all())
    
    