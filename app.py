from flask import Flask, request, jsonify
import datetime
import json

app = Flask(__name__)

# Function to log attack attempts
def log_attack(request):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ip": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "payload": str(request.data or request.form),
        "user_agent": request.headers.get('User-Agent')
    }
    with open('attack_logs.json', 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

# Fake login endpoint
@app.route('/login', methods=['POST', 'GET'])
def fake_login():
    log_attack(request)
    return "Invalid credentials!", 401

# Fake admin panel
@app.route('/admin')
def fake_admin_panel():
    log_attack(request)
    return "Unauthorized!", 403

# Fake API endpoint
@app.route('/api/users')
def fake_api():
    log_attack(request)
    return "Error: Invalid user ID", 400

# Trap file (e.g., backup.zip)
@app.route('/backup.zip')
def trap_file():
    log_attack(request)
    return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
