from flask import Flask
from flask_migrate import Migrate

from models import db

from init_data import load_categories, load_items

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)
migrate = Migrate(app, db)

from views import *

app.app_context().push()

#load_categories("delivery_categories")
#load_items("delivery_items")

if __name__ == "__main__":
    app.run()