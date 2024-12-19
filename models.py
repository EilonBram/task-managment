# # This file contains the table structure for users and tasks

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# # User Model: Represents users in the database
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # User ID (auto-increment)
#     username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
#     password = db.Column(db.String(128), nullable=False)  # Password (hashed)

# # Task Model: Represents tasks associated with users
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # Task ID (auto-increment)
#     description = db.Column(db.String(200), nullable=False)  # Task description
#     completed = db.Column(db.Boolean, default=False)  # Completion status (default: False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # User ID (foreign key)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))