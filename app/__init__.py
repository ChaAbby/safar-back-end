from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.itinerary import Itinerary
    from app.models.places import Places
    from app.models.tags import Tags

    from .routes import places_bp
    app.register_blueprint(places_bp)

    from .routes import tags_bp
    app.register_blueprint(tags_bp)

    from .routes import itinerary_bp
    app.register_blueprint(itinerary_bp)

    return app