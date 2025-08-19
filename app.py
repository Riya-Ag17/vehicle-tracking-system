from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Initial coordinates (Chennai)
lat = 13.0827
lng = 80.2707

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_location')
def get_location():
    global lat, lng
    # Simulate movement by adding a small random offset
    lat += (random.random() - 0.5) * 0.001
    lng += (random.random() - 0.5) * 0.001
    return jsonify({'lat': lat, 'lng': lng})

if __name__ == '__main__':
    app.run(debug=True)
