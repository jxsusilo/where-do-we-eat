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
    
    room1 = rooms[room_code]
    #prices = ['$', '$$', '$$$', '$$$$']
    prices = ['$$$$']
    room1.result('american', prices) 
    room1.restaurant_list()

    

    """
    for every restaurant in results: 
    if restaurant A is 'liked'
    get the cuisine of that restaurant
    incrememnt the count of that cuisine by 1 
    """
    
    