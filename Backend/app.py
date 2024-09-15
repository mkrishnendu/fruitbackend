from flask import Flask, jsonify
from flask_pymongo import PyMongo
from routes import init_routes
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize PyMongo
mongo = PyMongo(app)

# Initialize routes
init_routes(app, mongo)

# Add a default route for the root URL
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Fruit API!"})

if __name__ == '__main__':
    app.run(debug=True)