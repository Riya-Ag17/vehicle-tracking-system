from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# -------------------------------
# PostgreSQL Configuration
# -------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Berry@localhost/vehicle_tracking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------------
# Database Model
# -------------------------------
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(50), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    speed = db.Column(db.Float, nullable=True)

# Create tables
with app.app_context():
    db.create_all()

# -------------------------------
# Initial Location
# -------------------------------
lat, lng = 21.2514, 81.6296  # Raipur approx

# -------------------------------
# Routes
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location')
def get_location():
    global lat, lng
    lat += (random.random() - 0.5) * 0.001
    lng += (random.random() - 0.5) * 0.001
    speed = random.uniform(20, 60)  # Fake speed

    # Store / Update in DB
    vehicle = Vehicle.query.filter_by(vehicle_id="V001").first()
    if not vehicle:
        vehicle = Vehicle(vehicle_id="V001", latitude=lat, longitude=lng, speed=speed)
        db.session.add(vehicle)
    else:
        vehicle.latitude = lat
        vehicle.longitude = lng
        vehicle.speed = speed
    db.session.commit()

    return jsonify({
        'vehicle_id': "V001",
        'lat': lat,
        'lng': lng,
        'speed': speed
    })

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
