import base64
from flask import Flask, jsonify, request
from functools import wraps

from flask.wrappers import Response

app = Flask(__name__)
app.config.from_pyfile('settings.py')

def basic_auth_check(auth_header:str) -> bool:
    user = "aaron.williams"
    password ="iloveyou"
    encoded_credentials = auth_header.split()[-1].encode('utf-8')
    if encoded_credentials == base64.b64encode((user + ":" + password).encode('utf-8')):
        return True
    return False

def login_required(func):
    @wraps(func)
    def security_check(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and basic_auth_check(str(auth_header)):
            return func(*args, **kwargs)
        else:
            message = {'message':'You are not authorized to use this endpoint.'}
            return jsonify(message), 401
    return security_check

@app.route('/')
def home():
    message = {'message':'Welcome to the home endpoint!'}
    return jsonify(message)

@app.route('/basic_auth')
@login_required
def basic_auth():
    message = {'message':'Welcome to the basic_auth authenticated endpoint!'}
    return jsonify(message)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000)