# session.py
from api import FoodPicker 
import string
import random

#global dictionary
rooms = {

}
    



class Room:
    def __init__(self, location):
        self._room_id = self.code()
        self._participants = []
        self._restaurants = []
        self._location = location
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
            'thai': 0,
            'vietnamese': 0
        }

    def result(self, cuisine: str): 
        print('accessed')
        p = FoodPicker(self._location)
        data = p.get_restaurant_info(cuisine)
        yield from data


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

    def code(self) -> str: 
        '''Returns a room code of length max_len'''
        # would be nice to add checks to make sure the code 
        # doesn't already exist in the room 
        MAX_LEN = 6
        res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=MAX_LEN))
        return str(res)