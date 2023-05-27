class Restaurant: 
    def __init__(self, name, image_url, cuisine, price, rating, location):
        self.name = name
        self.image_url = image_url
        self.cuisine = cuisine 
        self.price = price
        self.rating = rating
        self.location = location 
        self.votes = 0

    def upvote_restaurant(self):
        self.votes += 1

    def downvote_restaurant(self):
        self.votes -= 1

    def all(self):
        return vars(self)