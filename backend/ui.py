from api import FoodPicker

def main():
    key = input("Enter key, or nothing if desired: ")
    if key: 
        location = input("Enter location: ")
        cuisine = input("Enter cuisine: ")

        p = FoodPicker(location, cuisine)
        p.set_api_key(key)
    else: 
        p = FoodPicker()
    
    print(p.result())

