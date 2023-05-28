class Restaurant: 
    def __init__(self, name, image_url, cuisine, price, rating, location):
        self.name = name
        self.image_url = image_url
        self.cuisine = cuisine 
        self.price = price
        self.rating = rating
        self.location = location 
        self.votes = 0

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other): 
        return self.name == other.name

    def upvote(self):
        self.votes += 1

    def downvote(self):
        self.votes -= 1

    def get_votes(self):
        return self.votes

    def all(self):
        return vars(self)