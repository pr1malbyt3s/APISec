from app import app
from flask import jsonify, request
from functools import wraps
from app.models import User
import base64
import bcrypt

def basic_auth_check(auth_header:str) -> bool:
    encoded_credentials = auth_header.split()[-1]
    decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
    creds = decoded_credentials.split(":")
    user, password = creds[0], creds[1]
    if(user and password):
        auth_user = User.query.filter_by(user=user).first()
        auth_pass = password.encode('utf-8')
        auth_salt = auth_user.salt.encode('utf-8')
        hashed_pass = bcrypt.hashpw(auth_pass, auth_salt).decode('utf-8')
        if(hashed_pass == auth_user.password):
            return True
    return False

def basic_auth_required(func):
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
@basic_auth_required
def basic_auth():
    message = {'message':'Welcome to the basic_auth authenticated endpoint!'}
    return jsonify(message)