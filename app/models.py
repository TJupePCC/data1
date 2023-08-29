from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fooditems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.String)
    item = db.Column(db.String)
    calories = db.Column(db.Integer)

    def to_dict(self):
        return {
            'restaurant': self.restaurant,
            'item': self.item,
            'calories': self.calories
        }
