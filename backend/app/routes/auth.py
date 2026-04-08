from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app.extensions import bcrypt, users_collection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if users_collection.find_one({"username": username}):
        return jsonify({"msg": "Username already exists"}), 400
        
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = {
        "username": username,
        "password_hash": hashed_password
    }
    users_collection.insert_one(new_user)
    return jsonify({"msg": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = users_collection.find_one({"username": username})
    if user and bcrypt.check_password_hash(user['password_hash'], password):
        user_id_str = str(user['_id'])
        access_token = create_access_token(identity=user_id_str) 
        return jsonify(access_token=access_token, user_id=user_id_str, username=user['username']), 200
        
    return jsonify({"msg": "Invalid username or password"}), 401

@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = users_collection.find()
    return jsonify([{"id": str(u['_id']), "username": u['username']} for u in users]), 200
