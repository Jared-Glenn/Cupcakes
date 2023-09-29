"""Models for Cupcakes API."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to the database."""
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Class Cupcake."""
    
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(100),
                       nullable=False)
    size = db.Column(db.String(100),
                     nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.String(1000),
                      nullable=False,
                      default="https://tinyurl.com/demo-cupcake")
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
        
    def __repr__(self):
        return f"<Cupcake {self.id} {self.flavor} {self.size} {self.rating} {self.image} >"