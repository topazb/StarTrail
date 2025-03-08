from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from google.oauth2 import id_token
from google.auth.transport import requests
import os
from db import get_db_connection

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Google OAuth Client ID (same as frontend)
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

@app.route('/auth/google', methods=['POST'])
def google_auth():
    token = request.json.get('token')
    if not token:
        return jsonify({"message": "Token is missing"}), 400

    try:
        # Verify the token
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        # Here, you can create a session or save user info in the database
        return jsonify({"message": "Token is valid", "user": id_info}), 200

    except ValueError:
        return jsonify({"message": "Invalid token"}), 400

@app.route('/test-db-connection')
def test_db_connection():
    try:
        result = get_db_connection()
        
        if result:
            return jsonify(result), 200  # Respond with JSON and HTTP status 200
        else:
            return jsonify(result), 500  # Respond with JSON and HTTP status 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
