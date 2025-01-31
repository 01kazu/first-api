from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = 'davidjoshua026@gmail.com'
GITHUB_URL = 'https://github.com/01kazu/MY-REPONAME' # PUT APPROPRIATE NAME


def get_current_datetime_iso():
    # Get current datetime
    utc_dt = datetime.now()
    # Convert UTC time to ISO 8601 format
    iso_date = utc_dt.isoformat()
    return iso_date

data = {'email': EMAIL_ADDRESS,
        'current_datetime': get_current_datetime_iso(),
        'github_url': GITHUB_URL}

@app.get("/data")
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)