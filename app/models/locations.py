from app import db


class Locations(db.Model):
    location_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat = db.Column(db.Integer)
    lon = db.Column(db.Integer)