"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Vehicle, Favorite_people, Favorite_planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Users 

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda User: User.serialize(), users))
    return jsonify(users), 200


@app.route('/users/<int:users_id>', methods=['GET'])
def get_users_by_id(users_id):
    users = User.query.get(users_id)
    return jsonify(users.serialize()), 200


@app.route('/users', methods=['POST'])
def create_users():
    users = User()
    users.email = request.json.get('email')
    users.password = request.json.get('password')
    users.is_active = request.json.get("is_active")
    users.save()
    return jsonify(users.serialize()), 201

#Favorite Planets
@app.route('/favorite_planet', methods=['GET'])
def get_favorites_planets():
    favorites_planets = Favorite_planet.query.all()
    favorites_planets = list(map(lambda Favorite_planet: Favorite_planet.serialize(), favorites_planets))
    return jsonify(favorites_planets), 200


@app.route('/favorite_planet/<int:users_id>', methods=['GET'])
def get_favorite_planets_by_id(users_id):
    favorite_planets = Favorite_planet.query.get(users_id, users_id)
    return jsonify(favorite_planets.serialize()), 200


@app.route('/favorite/planet', methods=['POST'])
def create_favorite_planet():
    favorite = Favorite_planet()
    favorite.planets_id = request.json.get('planets_id')
    favorite.users_id = request.json.get('users_id')
    favorite.save()
    return jsonify(favorite.serialize()), 201


@app.route('/favorite/planet/<int:planets_id>', methods=['DELETE'])
def delete_favorite_planet(planets_id):
    favorite = Favorite_planet.query.get(planets_id)
    favorite.delete()
    return jsonify(favorite.serialize()), 201

#Favorite People

@app.route('/favorite_people', methods=['GET'])
def get_favorite_people():
    favorite_people = Favorite_people.query.all()
    favorite_people = list(
        map(lambda Favorite_people: Favorite_people.serialize(), favorite_people))
    return jsonify(favorite_people), 200


@app.route('/favorite/people', methods=['POST'])
def create_favorite_people():
    favorite = Favorite_people()
    favorite.people_id = request.json.get('people_id')
    favorite.users_id = request.json.get('users_id')
    favorite.save()
    return jsonify(favorite.serialize()), 201


@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    favorite = Favorite_people.query.get(people_id)
    favorite.delete()
    return jsonify(favorite.serialize()), 201


#Planets 

@app.route("/planets", methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    planets = list(map(lambda Planet: Planet.serialize(), planets))
    return jsonify(planets), 200


@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planets_by_id(planets_id):
    planets = Planet.query.get(planets_id)
    return jsonify(planets.serialize()), 200


@app.route('/planets', methods=['POST'])
def create_planets():
    planets = Planet()
    planets.name = request.json.get('name')
    planets.climate = request.json.get('climate')
    planets.population = request.json.get('population')
    planets.terrain = request.json.get('terrain')
    planets.orbital_period = request.json.get('orbital_period')
    planets.rotation_period = request.json.get('rotation_period')
    planets.image = request.json.get('image')
    planets.save()
    return jsonify(planets.serialize()), 201


@app.route('/planets/<int:planets_id>', methods=['PUT'])
def update_planets(planets_id):
    planets = Planet.query.get(planets_id)
    planets.name = request.json.get('name')
    planets.climate = request.json.get('climate')
    planets.population = request.json.get('population')
    planets.terrain = request.json.get('terrain')
    planets.orbital_period = request.json.get('orbital_period')
    planets.rotation_period = request.json.get('rotation_period')
    planets.image = request.json.get('image')
    planets.update()
    return jsonify(planets.serialize()), 201


@app.route('/planets/<int:planets_id>', methods=['DELETE'])
def delete_planets(planets_id):
    planets = Planet.query.get(planets_id)
    planets.delete()
    return jsonify(planets.serialize()), 201

# People

@app.route("/people", methods=['GET'])
def get_people():
    people = People.query.all()
    people = list(map(lambda People: People.serialize(), people))
    return jsonify(people), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_by_id(people_id):
    people = People.query.get(people_id)
    return jsonify(people.serialize()), 200


@app.route('/people', methods=['POST'])
def create_people():
    people = People()
    people.name = request.json.get('name')
    people.description = request.json.get('description')
    people.thumbnail = request.json.get('thumbnail')
    people.image = request.json.get('image')
    people.save()
    return jsonify(people.serialize()), 201


@app.route('/people/<int:people_id>', methods=['PUT'])
def update_people(people_id):
    people = People.query.get(people_id)
    people.name = request.json.get('name')
    people.description = request.json.get('description')
    people.thumbnail = request.json.get('thumbnail')
    people.image = request.json.get('image')
    people.update()
    return jsonify(people.serialize()), 201


@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people(people_id):
    people = People.query.get(people_id)
    people.delete()
    return jsonify(people.serialize()), 201




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
