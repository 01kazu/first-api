from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = 'davidjoshua026@gmail.com'
GITHUB_URL = 'https://github.com/01kazu/first-api'


def get_current_datetime_iso():
    # Get current datetime for UTC
    utc_dt = datetime.now(timezone.utc)
    # Convert UTC time to ISO 8601 format
    iso_date = utc_dt.isoformat()
    return iso_date.strftime("%Y-%m-%dT%H:%M:%S%Z")

data = {'email': EMAIL_ADDRESS,
        'current_datetime': get_current_datetime_iso(),
        'github_url': GITHUB_URL}

@app.get("/data")
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
