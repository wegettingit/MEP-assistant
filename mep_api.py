from mep import query_mep  # Use lowercase if your file is named 'mep.py'
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for /api/*

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    print(f"\n[REQUEST] {user_input}")
    start = time.time()
    response = query_mep(user_input)
    elapsed = time.time() - start
    print(f"[RESPONSE] {response}\n[TIME] {elapsed:.2f} seconds")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
