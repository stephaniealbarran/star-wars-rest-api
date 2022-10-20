from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    climate = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.String(100), unique=False, nullable=False)
    terrain = db.Column(db.String(100), unique=False, nullable=False)
    orbital_period = db.Column(db.String(100), unique=False, nullable=False)
    rotation_period = db.Column(db.String(100), unique=False, nullable=False)
    image = db.Column(db.String(300), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "image": self.image
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    gender = db.Column(db.String(100), unique=False, nullable=False)
    height = db.Column(db.String(100), unique=True, nullable=False)
    birth_year = db.Column(db.String(100), unique=False, nullable=False)
    eye_color = db.Column(db.String(100), unique=False, nullable=False)
    image = db.Column(db.String(300), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "image": self.image

        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)
    vehicle_class = db.Column(db.String(100), unique=True, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)
    cost_in_credits = db.Column(db.String(100), unique=False, nullable=False)
    length = db.Column(db.String(300), unique=False, nullable=False)
    image = db.Column(db.String(300), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "image": self.image

        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favorite_people(db.Model):
    __tablename__ = 'favorite_people'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "people_id": self.people_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favorite_planet(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"))

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "planets_id": self.planets_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
