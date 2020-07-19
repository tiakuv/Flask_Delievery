from flask import render_template

from app import app
from models import db, Category, Dish
from forms import LoginForm, RegistForm

@app.route("/")
def main():
    categories = db.session.query(Category).all()
    dishes=[]
    for cat in categories:
        dishes_ = db.session.query(Dish).filter(Dish.category_id == cat.id).limit(3)
        for d in dishes_:
            dishes.append(d)
    return render_template("main.html", categories=categories, dishes=dishes)

@app.route("/login/")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register/")
def register():
    form = RegistForm()
    return render_template("register.html", form=form)