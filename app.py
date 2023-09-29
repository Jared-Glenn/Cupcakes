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
