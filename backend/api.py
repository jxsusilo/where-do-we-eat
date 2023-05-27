#api.py

import json 
import urllib.parse
from pip._vendor import requests

class FoodPicker:
    def __init__(self, location = None, cuisine = None):
        self._base_url = 'https://api.yelp.com/v3/businesses/search'
        self._location = location
        self._cuisine = cuisine
        self._api_key = None
        self._MAX_RESULTS = 10

    def set_api_key(self, key):
        self._api_key = key
        
    def header(self) -> dict:
        key_phrase = "Bearer " + self._api_key
        headers = {"accept": "application/json",
                   "Authorization": key_phrase}
        return headers
        
    def url(self): 
        params = {'location': self._location, 'categories': self._cuisine, 'sort_by': 'best_match', 'limit': self._MAX_RESULTS}
        temp = urllib.parse.urlencode(params)
        return self._base_url +'?'+ temp

    def result(self) -> str: 
        if not self._api_key:  
            with open('mock.json', "r") as f:
                data = json.load(f)
            return data
        else: 
            response = requests.get(self.url(), headers=self.header())
            return response.text