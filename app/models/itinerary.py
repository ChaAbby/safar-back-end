from app import db


class Itinerary(db.Model):
    itinerary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    itinerary_name = db.Column(db.String)
    location = db.Column(db.String)