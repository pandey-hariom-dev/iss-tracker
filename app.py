from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/position')
def get_position():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
        data = response.json()
        lat = float(data['iss_position']['latitude'])
        long = float(data['iss_position']['longitude'])
        return jsonify({"latitude": lat, "longitude": long})
    except:
        return "⚠️Connection failed, retrying..."

if __name__ == '__main__':
    app.run(debug=True)