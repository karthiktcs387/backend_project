from flask import Flask
from flask_cors import CORS 
from models import db
from routes.auth import auth_bp
from routes.opportunity import opp_bp

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ✅ Register route
app.register_blueprint(auth_bp)
app.register_blueprint(opp_bp)

@app.route('/')
def home():
    return "Backend is working!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)