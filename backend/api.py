#api.py
from pathlib import Path
script_path = Path(__file__, '..').resolve()
import json 
import urllib.parse
from pip._vendor import requests

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
        
    def url(self, cuisine: str): 
        # limit will change based on cuisine
        # let's say 10 ppl are deciding, 6 ppl choose italian and 4 ppl choose american
        # we'd wanna display 6 italian results and 4 american results 

        params = {'location': self._location, 'categories': cuisine, 'sort_by': 'best_match', 'limit': self._MAX_RESULTS}
        temp = urllib.parse.urlencode(params)
        return self._base_url +'?'+ temp

    def result(self, cuisine: str) -> str: 
        if not self._api_key:  
            with open(script_path.joinpath("mock.json"), "r") as f:
                results = json.load(f)
                data = self.filter(cuisine, results)
                yield from data
        else: 
            response = requests.get(self.url(cuisine), headers=self.header())
            data = response.text
            results = self.filter(cuisine, json.loads(data))
            yield from results

    def filter(self, cuisine, data: json):
        if "businesses" in data: 
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
                yield name, image_url, cuisine, price, rating, location