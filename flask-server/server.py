import sys
import os

# Add the project root directory to the Python path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend import generator

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Hey, everything works!!'})


@app.route("/members")
def members():
    return jsonify({"members": ["Member1", "Member2", "Member3"]})

#they don't have a session id~
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get the JSON data from the request
    checked_cuisine_list = data.get('checkedCuisine')
    checked_price_list = data.get('checkedPrice')
    room_code = data.get('roomCode')
    print(checked_cuisine_list, checked_price_list, room_code)
    restaurant_set = list()

    #TEMP CODE!! when we get the final, we shouldnt be submitting unexisting room codes
    try:
        roomvar = generator.rooms[room_code]
    except:
        print('room doesnt exist')
        print('making sample room')
        roomvar = generator.Room("irvine", room_code)
        generator.rooms[room_code] = roomvar

    # roomvar = generator.Room("irvine", 'adkjhkfh')
    for a in roomvar.result(checked_cuisine_list, checked_price_list):
        restaurant_set.append(a)
    
    response = {'message': 'Data received successfully', 'info':restaurant_set}
    return response, 200

@app.route('/get-participants', methods=['POST'])
def get_participants():
    data = request.get_json() 
    room_code = data.get('roomCode')
    print(room_code)

    #TEMP CODE!! when we get the final, we shouldnt be submitting unexisting room codes
    try:
        roomvar = generator.rooms[room_code]
    except:
        print('room doesnt exist')
        print('making sample room')
        roomvar = generator.Room("irvine", room_code)
        generator.rooms[room_code] = roomvar

    response = {'message': 'Data received successfully', 'info':roomvar._participants}
    return response, 200


# if they already have a session id getting/updating
@app.route('/:sessionCode',methods=['GET'])
def getdata(sessionCode):
    return generator.rooms[sessionCode]


if __name__ == '__main__':
    app.run()

if __name__ == "__main__":
    app.run(debug=True)
    print("run")