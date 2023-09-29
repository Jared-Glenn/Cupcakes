"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
db.create_all()


@app.route('/api/cupcakes', methods=["GET"])
def all_cupcakes():
    """Give all the cupcakes on the site."""
    
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<cupcake_id>', methods=["GET"])
def get_cupcake(cupcake_id):
    """Get the identified cupcake."""
    
    cupcake = (Cupcake.query.get_or_404(cupcake_id)).serialize()
    
    return jsonify(cupcake=cupcake)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a new cupcake."""
    
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], 
                          rating=request.json["rating"], image=request.json["image"])
    
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update the specified cupcake."""
    
    