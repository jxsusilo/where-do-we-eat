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

    response = {'message': 'Data received successfully'}
    print(response)
    return response, 200 



#preferences with a session id
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get the JSON data from the request
    checked_list = data.get('checked')
    #price_list = data.get('price')
    print(checked_list)
    #print(price_list)
    restaurant_set = list()

    if room_flag == 1:
        #existing room
        pass
    else: 
        #new room 
        for a in roomvar.result(checked_list[0],['$', '$$', '$$$', '$$$$']):
            restaurant_set.append(a)

    

    response = {'message': 'Data received successfully', 'info':restaurant_set}
    print(response)
    return response, 200


# if they already have a session id getting/updating
@app.route('/:sessionCode',methods=['GET'])
def getdata(sessionCode):
    return generator.rooms[sessionCode]




if __name__ == "__main__":
    app.run(debug=True)
    print("run")