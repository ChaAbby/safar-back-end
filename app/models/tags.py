from app import db


class Tags(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String)


    def to_json_tags(self):
            return {
                "tag_id": self.tag_id,
                "type": self.type,
                }