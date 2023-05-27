# generator.py
import string
import random

#global dictionary
rooms = {

}
    
def code() -> str: 
    '''Returns a room code of length max_len'''
    # would be nice to add checks to make sure the code 
    # doesn't already exist in the room 
    MAX_LEN = 6
    res = ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k=MAX_LEN))
    return str(res)


class Room:
    def __init__(self, code):
        self._room_id = code
        self._participants = []
        self._restaurants = []
        self._cuisines = {
            'american': 0,
            'chinese' : 0,
            'greek': 0,
            'indian': 0,
            'italian': 0,
            'japanese': 0,
            'korean': 0,
            'mexican': 0,
            'nigerian': 0,
            'thai': 0
        }
        
    def update_data(self):
        global rooms
        internal = {'participants': self._participants, 
                    'cuisines': self._cuisines,
                    'restaurants': self._restaurants
        }
        rooms[self._room_id] = internal

    def add_particpant(self, participant: str):
        self._participants.append(participant)

    def vote_cuisine(self, cuisine):
        for cui, count in self._cuisines.items(): 
            if cui == cuisine.lower(): 
                self._cuisines[cui] += 1

    def add_restaurant(self, restaurant: str):
        self._restaurants.append(restaurant)