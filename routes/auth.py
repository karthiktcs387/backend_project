from flask import Blueprint, request, jsonify
from models import db, Admin
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# ✅ SIGNUP
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json

    # Validation
    if not data.get('full_name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "All fields required"}), 400

    if len(data['password']) < 8:
        return jsonify({"error": "Password must be 8 characters"}), 400

    # Check existing email
    if Admin.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Account already exists"}), 400

    hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user = Admin(
        full_name=data['full_name'],
        email=data['email'],
        password=hashed
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Signup successful"})


# ✅ LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = Admin.query.filter_by(email=data['email']).first()

    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({
        "message": "Login successful",
        "admin_id": user.id
    })