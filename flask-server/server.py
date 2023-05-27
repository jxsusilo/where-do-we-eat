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


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get the JSON data from the request
    checked_list = data.get('checked')
    print(checked_list)
    restaurant_set = list()

    roomvar = generator.Room("irvine")
    for a in roomvar.result(checked_list[0],['$', '$$', '$$$', '$$$$']):
        restaurant_set.append(a)

    response = {'message': 'Data received successfully', 'info':restaurant_set}
    return response, 200




if __name__ == '__main__':
    app.run()

if __name__ == "__main__":
    app.run(debug=True)
    print("run")