from app import db


class Itinerary(db.Model):
    itinerary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    itinerary_name = db.Column(db.String)
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'), nullable = True)

    def to_json_itin(self):
        return {
                "itinerary_id": self.itinerary_id,
                "itinerary_name": self.itinerary_name,
                "place_id": self.place_id,
            }