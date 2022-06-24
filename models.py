"""Models for Adopt."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

defaultProfile = "https://images.squarespace-cdn.com/content/v1/540a27e8e4b042802a33c882/1516384291548-W46CZ9A6R0M6OOC49QUA/catBoarding.png"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def default_image(self):
        return self.photo_url or defaultProfile
