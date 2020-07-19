import csv

from models import db, Category, Dish


def load_categories(file):
    with open(f'{file}.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = Category(title=row['title'])
            db.session.add(category)
        db.session.commit()


def load_items(file):
    with open(f'{file}.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dish = Dish(title=row['title'], price=row['price'], description=row['description'],
                        picture=row['picture'], category_id=row['category_id'])
            db.session.add(dish)
        db.session.commit()