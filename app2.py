from flask import Flask, jsonify

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

# Flask setup
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    print("Retrieving homepage")
    return "Welcome to my home page"

@app.route("/api/justice_league")
def all_justice():
    """Return a list of all passenger names"""

    print("Retrieving justice league API")
    return jsonify(justice_league_members)


if __name__ == '__main__':
    app.run(debug=False)