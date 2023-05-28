# session.py
import sys
import os

# Add the project root directory to the Python path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)
from backend.restaurant import Restaurant 
from backend.api import FoodPicker 

#global dictionary
rooms = {

}

class Room:
    def __init__(self, location, code):
        self._room_id = code
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
        self.update_data()

<<<<<<< HEAD
    def result(self, cuisine: str, price: list[str], number): 
        p = FoodPicker(self._location)
        #api_key = input("Enter apikey: ")
        #if len(api_key) > 0:
            #p.set_api_key(api_key)
        data = p.result(cuisine, price, number)
        self._restaurants.extend(data)
=======
    def result(self, cuisine: list[str], price: list[str]): 
        p = FoodPicker(self._location)
        api_key = input("Enter apikey: ")
        if len(api_key) > 0:
            p.set_api_key(api_key)
        data = p.cuisine_from_list(cuisine, price)
        self._restaurants = data
>>>>>>> refs/remotes/origin/main

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

    def vote(self, number: int, direction: int):
        restaurant = self._restaurants[number-1] 
        if (direction < 0): 
            restaurant.downvote()
        elif (direction > 0):
            restaurant.upvote()

    def show_restaurant_list(self):
        desc = sorted(self._restaurants, key = lambda x: x.votes, reverse=True)
        self._restaurants = desc
        for r in range(len(desc)): 
            print(r+1,') ', desc[r].name, ' (',desc[r].votes,')', sep ='')

    def all_votes(self):
        total = 0 
        for val in self._cuisines.values(): 
            total += val
        return total