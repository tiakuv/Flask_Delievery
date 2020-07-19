from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, unique=True)
    orders = db.relationship('Order', back_populates="user")  # 1 to many


class Dish(db.Model):
    __tablename__ = "dishes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    picture = db.Column(db.String, unique=True, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    categories = db.relationship('Category', back_populates="dishes")

    orders = db.relationship('Order', back_populates="dishes")

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)

    dishes = db.relationship('Dish', back_populates="categories")


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    ammount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'))
    dishes = db.relationship('Dish', back_populates="orders")

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates="orders")