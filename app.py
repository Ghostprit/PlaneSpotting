from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/flights')
def get_flights():
    url = 'https://opensky-network.org/api/states/all?lamin=53.8&lomin=20.9&lamax=56.5&lomax=26.9'
    response = requests.get(url, timeout=5)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)