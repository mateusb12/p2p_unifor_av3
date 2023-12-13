from flask import Flask, jsonify

from technologies.mock_data import users, posts

app = Flask(__name__)


# Mock data


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id, {})
    return jsonify(user)


# Endpoint to get user's friends
@app.route('/users/<user_id>/friends', methods=['GET'])
def get_user_friends(user_id):
    user = users.get(user_id, {})
    friends = [users.get(fid, {}) for fid in user.get("friends", [])]
    return jsonify(friends)


# Endpoint to get user's posts
@app.route('/users/<user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    user = users.get(user_id, {})
    user_posts = [posts.get(pid, {}) for pid in user.get("posts", [])]
    return jsonify(user_posts)


if __name__ == '__main__':
    PORT = 8000
    app.run(debug=True, port=PORT)
