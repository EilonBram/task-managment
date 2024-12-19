from flask import Blueprint, request, jsonify
from models import db, User, Task
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Create a Blueprint for routes
routes = Blueprint('routes', __name__)



@routes.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask server is running"}), 200


@routes.route('/register', methods=['POST'])
def register():
    # Strictly accept JSON
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid input, JSON expected"}), 400

    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Check for existing user
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    # Save the new user with a hashed password
    try:
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"id": new_user.id, "username": new_user.username}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), 500


@routes.route('/login', methods=['POST'])
def login():
    # Support both application/json and form-urlencoded
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    username = data.get('username')
    password = data.get('password')

    # Find the user in the database
    user = User.query.filter_by(username=username).first()

    # Check if user exists and the password matches
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user.id))

    # Return the token with a 200 status code
    return jsonify({"access_token": access_token}), 200


# Create Task
@routes.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    description = data.get('description')
    user_id = get_jwt_identity()

    if not description:
        return jsonify({"message": "Description is required"}), 400

    new_task = Task(description=description, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({
    "id": new_task.id,
    "description": new_task.description,
    "completed": new_task.completed,
    "user_id": int(user_id)
}), 200


# Get Tasks
@routes.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    # return jsonify([{"id": task.id, "description": task.description, "completed": task.completed} for task in tasks]), 200
    return jsonify([
    {"id": task.id, "description": task.description, "completed": task.completed, "user_id": task.user_id}
    for task in tasks
]), 200


# Update Task
@routes.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    data = request.get_json()
    description = data.get('description')
    completed = data.get('completed')
    user_id = get_jwt_identity()

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    if description is not None:
        task.description = description
    if completed is not None:
        task.completed = completed

    db.session.commit()
    
    return jsonify({"id": task.id, "description": task.description, "completed": task.completed}), 200

# Delete Task
@routes.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200

# Delete User
@routes.route('/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200
