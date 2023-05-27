from flask import Flask,request
from flask_cors import CORS
from backend import api 
app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get the JSON data from the request
    checked_list = data.get('checked')
    print(checked_list)
    
    for food_item in checked_list: 
        foodvar = api.FoodPicker(cuisine=checked_list[food_item])
        return foodvar.get_restaurant() #return restraunt json data

    response = {'message': 'Data received successfully'}
    return response, 200

if __name__ == '__main__':
    app.run()

if __name__ == "__main__":
    app.run(debug=True)
    print("run")