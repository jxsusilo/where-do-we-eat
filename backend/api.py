#api.py

import json 
import urllib.parse
from pip._vendor import requests

class FoodPicker:
    def __init__(self, location = None):
        self._base_url = 'https://api.yelp.com/v3/businesses/search'
        self._location = location
        self._api_key = None
        self._MAX_RESULTS = 10

    def set_api_key(self, key):
        self._api_key = key
        
    def header(self) -> dict:
        key_phrase = "Bearer " + self._api_key
        headers = {"accept": "application/json",
                   "Authorization": key_phrase}
        return headers
        
    def url(self, cuisine: str): 
        # limit will change based on cuisine
        # let's say 10 ppl are deciding, 6 ppl choose italian and 4 ppl choose american
        # we'd wanna display 6 italian results and 4 american results 

        params = {'location': self._location, 'categories': cuisine, 'sort_by': 'best_match', 'limit': self._MAX_RESULTS}
        temp = urllib.parse.urlencode(params)
        return self._base_url +'?'+ temp

    def result(self, cuisine: str) -> str: 
        if not self._api_key:  
            with open('mock.json', "r") as f:
                data = json.load(f)
            return data
        else: 
            response = requests.get(self.url(cuisine), headers=self.header())
            return response.text
    
    def get_resturant_info(data):
        if "businesses" in data:
            resturant = data['business'][0]
            name = resturant['name']
            image_url = resturant['image_url']
            cuisine = resturant['categories']['alias']
            rating = resturant['rating']
            price = resturant['price']
            location = resturant['location']['display_address']

            return name, image_url, cuisine, rating, price, location