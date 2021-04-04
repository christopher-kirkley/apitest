from flask import Flask
from flask import request, jsonify

import jwt
from functools import wraps

app = Flask(__name__)
app.config["DEBUG"] = True

key = "secret"

""" Some dummy json data """
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
   
    return decorated 

@app.route('/tasks', methods=['GET'])
@token_required
def home():
    return jsonify({'tasks': tasks})


if __name__ == "__main__":
    app.run()
