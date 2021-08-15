from app import db
from decimal import Decimal

class Places(db.Model):
    place_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat = db.Column(db.Numeric(precision=None, scale=None, decimal_return_scale=None, asdecimal=True))
    lng = db.Column(db.Numeric(precision=None, scale=None, decimal_return_scale=None, asdecimal=True))
    total = db.Column(db.Numeric(precision=None, scale=None, decimal_return_scale=None, asdecimal=True))
    name = db.Column(db.String)
    # origin = db.Column(db.Boolean(create_constraint=False, name=None, _create_events=True))
    google_place_id = db.Column(db.String)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.itinerary_id'), nullable = True)

    def to_json(self):
        return {
                "place_id": self.place_id,
                "lat": str(self.lat),
                "lng": str(self.lng),
                "total": str(self.total),
                "name": self.name,
                "google_place_id": self.google_place_id,
                # "origin": self.origin,
                "itinerary_id" : self.itinerary_id
                }