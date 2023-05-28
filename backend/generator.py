# session.py
import sys
import os

# Add the project root directory to the Python path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)
from backend.restaurant import Restaurant 
from backend.api import FoodPicker 
import math

#global dictionary
rooms = {}

MAX_CHOICES = 10

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

    def result(self, cuisine: str, price: list[str], number): 
        p = FoodPicker(self._location)
        data = p.result(cuisine, price, number) #new api data
        filtered = []
        for e in data: 
            if not self.has_same(e):
                filtered.append(e)
        filtered.extend(self._restaurants)
        filtered = filtered[:MAX_CHOICES]
        self._restaurants = sorted(filtered, key = lambda x: x.votes, reverse=True)
        
    def has_same(self, obj: Restaurant) -> bool: 
        for x in self._restaurants: 
            if obj == x:
                return True
        return False
        
    def give_final_results(self, cuisines, price) -> None: 
        for c in cuisines:
            c = c.lower()
            try: 
                listings = math.ceil((self._cuisines[c]/(self.all_votes()))*10)
            except ZeroDivisionError: 
                listings = MAX_CHOICES

            if listings > 1:
                self.result(c, price, listings)
            else:
                self.result(c, price, MAX_CHOICES)

    def update_data(self):
        global rooms
        rooms[self._room_id] = self

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
        for r in range(len(self._restaurants)): 
            print(r+1,') ', self._restaurants[r].name, ' (',self._restaurants[r].votes,')', sep ='')

    def all_votes(self):
        total = 0 
        for val in self._cuisines.values(): 
            total += val
        return total