from app import db


class Itinerary(db.Model):
    itinerary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.Integer)
    location = db.Column(db.String)