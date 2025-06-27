from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)


users = []
nextId = 1  # Auto-increment ID


# 1. Get all users
@app.route('/', methods=['GET'])
def getAllUsers():
    return jsonify(users), 200


# 2. Get a single user by ID
@app.route('/userSearch/<int:userId>', methods=['GET'])
def getUser(userId):
    for user in users:
        if user['id'] == userId:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# 3. Create a new user
@app.route('/user', methods=['POST'])
def create_user():
    global nextId
    data = request.get_json()
    # Basic validation
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400

    new_user = {
        "id": nextId,
        "name": data['name'],
        "email": data['email'],
        "password": data.get('password', '')  # In real app: hash this!
    }
    users.append(new_user)
    nextId += 1
    return jsonify(new_user), 201

# Add new user
@app.route('/newUser', methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'POST':
        global nextId
        data = request.get_json() or request.form
        if not data.get('name') or not data.get('email'):
            return jsonify({"error": "Name and email are required"}), 400

        new_user = {
            "id": nextId,
            "name": data['name'],
            "email": data['email'],
            "password": data.get('password', '')
        }
        users.append(new_user)
        nextId += 1
        return jsonify(new_user), 201
    else:
        return send_from_directory(os.path.dirname(__file__), 'add_user.html')


# 4. Update the user completely
@app.route('/update/<int:userId>', methods=['PUT'])
def update_user(userId):
    data = request.get_json()
    for user in users:
        if user['id'] == userId:
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            user['password'] = data.get('password', user['password'])
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/update')
def serve_update_user():
    return send_from_directory(os.path.dirname(__file__), 'update_user.html')


# Delete the user
@app.route('/delete/<int:userId>')
def delete_user(userId):
    for i, user in enumerate(users):
        if user['id'] == userId:
            users.pop(i)
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

