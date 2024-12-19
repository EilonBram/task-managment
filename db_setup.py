#This file sets up the database using SQLite. It initializes the database and creates the tables if they don't exist.
#  the create_app() function initializes the Flask app, configures the database, and creates the tables using the db.create_all() method. The app.app_context() block ensures that the database is created within the application context.

from flask import Flask
from models import db

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables

    return app
