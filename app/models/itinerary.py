from app import db


class Itinerary(db.Model):
    itinerary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    itinerary_name = db.Column(db.String)
    places = db.relationship('Places', backref='itinerary', lazy=True, order_by = "Places.total")

    def to_json_itin(self):
        return {
                "itinerary_id": self.itinerary_id,
                "itinerary_name": self.itinerary_name
            }