import sys
import os

# Add the project root directory to the Python path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend import generator, ui

app = Flask(__name__)
CORS(app)
 

@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})


@app.route("/members")
def members():
    return jsonify({"members": ["Member1", "Member2", "Member3"]})


#create a room with/witout a room code
@app.route("/setup", methods=['POST'])
def roomGeneration(): 
    global roomvar
    global roomCode
    global room_flag
    
    

    data = request.get_json()  # Get the JSON data from the request
    location = data.get('location')
    code = data.get('roomcode')
    name = data.get('name')
    
    if code == 0: 
        # new room
        print("new room")
        roomCode = ui.code()
        print(roomCode)
        roomvar = generator.Room(location,roomCode)
        print(generator.rooms)
        room_flag = 0
    else:
        # existing room
        print("existing room")
        roomCode = code
        roomvar = generator.rooms[roomCode]
        room_flag = 1
    roomvar.add_particpant(name)
    print(roomvar._participants)

    response = {'message': 'Data received successfully', 'code': roomCode}
    print(response)
    return response, 200 



#preferences with a session id
@app.route('/submit', methods=['POST'])
def submit():
    global checked_price_list
    data = request.get_json()  # Get the JSON data from the request
    checked_cuisine_list = data.get('checkedCuisine')
    checked_price_list = data.get('checkedPrice')
    room_code = data.get('roomCode')
    print(checked_cuisine_list, checked_price_list, room_code)
    restaurant_list = list()

    #TEMP CODE!! when we get the final, we shouldnt be submitting unexisting room codes
    # try:
    #     roomvar = generator.rooms[room_code]
    # except:
    #     print('room doesnt exist')
    #     print('making sample room')
    #     roomvar = generator.Room("irvine", room_code)
    #     #generator.rooms[room_code] = roomvar

    # roomvar = generator.Room("irvine", 'adkjhkfh')
    roomvar = generator.rooms[room_code]
    #print(generator.rooms)
    #print(roomvar)
    for cuisine in checked_cuisine_list:
        roomvar.vote_cuisine(cuisine)
    results = roomvar.give_final_results(checked_cuisine_list, checked_price_list)
    for r in roomvar._restaurants:
        print(r.name)
        restaurant_list.append(
            r.all()
            # {
            #     'name': r.name,
            #     'image_url': r.image_url,
            #     'cuisine': r.cuisine,
            #     'price': r.price,
            #     'rating': r.rating,
            #     'location': r.location,
            #     'votes': r.votes
            # }
        )
    
    #for a in roomvar.result(checked_cuisine_list, checked_price_list):
        #restaurant_set.append(a)
    
    response = jsonify({"restaurants": restaurant_list})
    #print(restaurant_list)
    return response, 200

@app.route('/get-participants', methods=['POST'])
def get_participants():
    data = request.get_json() 
    room_code = data.get('roomCode')
    print(room_code)

    #TEMP CODE!! when we get the final, we shouldnt be submitting unexisting room codes
    # try:
    #     roomvar = generator.rooms[room_code]
    # except:
    #     print('room doesnt exist')
    #     print('making sample room')
    #     roomvar = generator.Room("irvine", room_code)
    #     #generator.rooms[room_code] = roomvar

    response = {'message': 'Data received successfully', 'info':roomvar._participants}
    return response, 200

@app.route('/get-restaurants', methods=['POST'])
def getRestaurants():
    data = request.get_json() 
    room_code = data.get('roomCode')
    restaurant_list = []

    #TEMP CODE!! when we get the final, we shouldnt be submitting unexisting room codes
    # try:
    #     roomvar = generator.rooms[room_code]
    # except:
    #     print('room doesnt exist')
    #     print('making sample room')
    #     roomvar = generator.Room("irvine", room_code)
    #     #generator.rooms[room_code] = roomvar

    results = roomvar._restaurants
    for r in results:
        restaurant_list.append(
            r.all()
        )
    response = jsonify({"restaurants": restaurant_list})
    print(restaurant_list)
    return response

@app.route('/upvote', methods=['POST'])
def upvote():
    data = request.get_json()  # Get the JSON data from the request
    name = data.get('restaurant')
    for i in range(len(roomvar._restaurants)):
        if roomvar._restaurants[i].name == name:
            restraunt_index = i
    cusine_lst = [name for name,val in roomvar._cuisines.items() if val >= 1]
    roomvar.vote(restraunt_index+1, 1) 
    roomvar.give_final_results(cusine_lst,checked_price_list)
    #print(roomvar._cuisines.items())
    #print(checked_price_list)
    roomvar.show_restaurant_list()
    
    restaurant_list = list()
    for r in roomvar._restaurants:
        restaurant_list.append(r.all())
     
    response = jsonify({"restaurants": restaurant_list})
    #print(restaurant_list)
    return response, 200

@app.route('/downvote', methods=['POST'])
def downvote(): 
    data = request.get_json()  # Get the JSON data from the request
    name = data.get('restaurant')
    for i in range(len(roomvar._restaurants)):
        if roomvar._restaurants[i].name == name:
            restraunt_index = i
    roomvar.vote(restraunt_index+1, -1)
    cusine_lst = [name for name,val in roomvar._cuisines.items() if val >= 1]
    roomvar.give_final_results(cusine_lst,checked_price_list)
    #print(roomvar._cuisines.items())
    #print(checked_price_list)
    roomvar.show_restaurant_list()
    
    restaurant_list = list()
    for r in roomvar._restaurants:
        restaurant_list.append(r.all())
     
    response = jsonify({"restaurants": restaurant_list})
    #print(restaurant_list)
    return response, 200
    

# if they already have a session id getting/updating
@app.route('/:sessionCode',methods=['GET'])
def getdata(sessionCode):
    return generator.rooms[sessionCode]




if __name__ == "__main__":
    app.run(debug=True)
    print("run")