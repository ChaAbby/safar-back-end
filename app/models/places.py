from app import db


class Places(db.Model):
    place_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    name = db.Column(db.String)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'), nullable = True)