from flask import Flask, jsonify, render_template
import numpy as np
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Grab connection URL from local environment variables
connection_var = os.environ.get("mysql_connection")
engine = create_engine(connection_var)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Justice = Base.classes.justice_league
# Avengers = Base.classes.avengers

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask setup
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    print("Retrieving homepage")
    return "Welcome to my hompage"

@app.route("/api/justice_league")
def all_justice():
    """Return a list of all passenger names"""
    print("Retrieving justice league API")
    # Query all passengers
    results = session.query(Justice).all()

    # Convert list of tuples into normal list
    all_superheros = []
    for superhero in results:
        superhero_dict = {}
        superhero_dict["superhero"] = superhero.superhero
        superhero_dict["real_name"] = superhero.real_name
        all_superheros.append(superhero_dict)

    return jsonify(all_superheros)

@app.route("/api/avengers")
def all_avengers():
    """Return a list of all passenger names"""
    print("Retrieving avengers API")
    # Query all passengers
    Avengers = Base.classes.avengers
    results = session.query(Avengers).all()

    # Convert list of tuples into normal list
    all_superheros = []
    for superhero in results:
        superhero_dict = {}
        superhero_dict["superhero"] = superhero.superhero
        superhero_dict["real_name"] = superhero.real_name
        all_superheros.append(superhero_dict)

    return jsonify(all_superheros)


if __name__ == '__main__':
    app.run(debug=False)
