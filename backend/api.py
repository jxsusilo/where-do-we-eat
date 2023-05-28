#api.py
import sys
import os

# Add the project root directory to the Python path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from pathlib import Path
script_path = Path(__file__, '..').resolve()
import json 
import urllib.parse
from pip._vendor import requests
from backend.restaurant import Restaurant

cuisines = {
            'american',
            'chinese',
            'greek',
            'indian',
            'italian',
            'japanese',
            'korean',
            'mexican',
            'nigerian',
            'thai',
            'vietnamese'
        }

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
        
    def translate_price(self, price: list[str]) -> str: 
        int_rep = [len(x) for x in price]
        params = '&'
        for p in int_rep: 
            params += 'price='+ str(p)+ '&'
        return params[:-1]

    def url(self, cuisine: str, price: list) -> str: 
        # limit will change based on cuisine
        # let's say 10 ppl are deciding, 6 ppl choose italian and 4 ppl choose american
        # we'd wanna display 6 italian results and 4 american results 

        params = {'location': self._location, 'categories': cuisine, 'sort_by': 'best_match', 'limit': self._MAX_RESULTS}
        temp = urllib.parse.urlencode(params) + self.translate_price(price)
        return self._base_url +'?'+ temp
    
    def cuisine_from_list(self, cuisine: list['str'], price: list[str]): 
        total = []
        for c in cuisine: 
            results = self.result(c, price)
            if type(results) == list: 
                total.extend(results)
        return total 


    def result(self, cuisine: str, price: list[str]) -> list[Restaurant] | str: 
        if not self._api_key:  
            try: 
                with open(script_path.joinpath("mock.json"), "r") as f:
                    results = json.load(f)
                    data = self.filter(cuisine, results)
                    return data
            except FileNotFoundError:
                return "Error: mock.json file not found"
        else: 
            try: 
                response = requests.get(self.url(cuisine, price), headers=self.header())
                data = response.text
                results = self.filter(cuisine, json.loads(data))
                return results
            except requests.RequestException as e:
                return ("Error: ", e)
    
    def filter(self, cuisine, data: json) -> list[Restaurant]:
        if "businesses" in data: 
            results = []
            for res in data['businesses']:
                name = res['name']
                image_url = res['image_url']
                categories = res["categories"]
                for category in categories:
                    alias = category["alias"]
                    if alias in cuisines:
                        cuisine = alias
                rating = res['rating']
                try: 
                    price = res['price']
                except KeyError: 
                    price = None
                location = res['location']['display_address']

                results.append(Restaurant(name, image_url, cuisine, price, rating, location))
            return results
        else: 
            return "Data could not be retrieved."