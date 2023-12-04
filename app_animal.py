from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Hello World Endpoint
@app.route('/')
def hello_world():
    return 'Hello Animal World!'

# Get All Animals Endpoint
@app.route('/animals', methods=['GET'])
def get_all_animals():
    with open('animals_data.json', 'r') as file:
        animals = json.load(file)
    return jsonify(animals)

# Filter Animals Endpoint
@app.route('/animals', methods=['GET'])
def filter_animals():
    filter_value = request.args.get('filter')
    with open('animals_data.json', 'r') as file:
        animals = json.load(file)
    filtered_animals = [animal for animal in animals if filter_value.lower() in animal.values()]
    return jsonify(filtered_animals)

# Get Specific Animal Endpoint
@app.route('/animal/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    with open('animals_data.json', 'r') as file:
        animals = json.load(file)
    for animal in animals:
        if animal.get('id') == animal_id:
            return jsonify(animal)
    return jsonify({'error': 'Animal not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
