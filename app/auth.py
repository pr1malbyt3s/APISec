from app.models import User
from app import app
from flask import request
from functools import wraps
import base64
import bcrypt
import jwt

def basic_auth_required(func):
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
    
    @wraps(func)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if(auth_header):
            try:
                if(basic_auth_check(str(auth_header))):
                    return func(*args, **kwargs)
                else:
                    message = {'message':'You are not authorized to use this basic_auth endpoint.'}
                    return message, 401
            except:
                message = {'message':'You are not authorized to use this basic_auth endpoint.'}
                return message, 401
        else:
            message = {'message':'You did not provide credentials to access this basic_auth endpoint.'}
            return message, 401
    return decorated

def jwt_token_required(func):
    def jwt_check(auth_header:str) -> bool:
        encoded_token = auth_header.split()[-1]
        #decoded_token = jwt.decode(encoded_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        # Signature not being verified here:
        decoded_token = jwt.decode(encoded_token, algorithms=['HS256'])
        auth_user = User.query.filter_by(id=decoded_token['id']).first()
        if(auth_user):
            return True
        return False

    @wraps(func)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if(auth_header):
            try:
                if(jwt_check(str(auth_header))):
                    return func(*args, **kwargs)
                else:
                    message = {'Error':'Insufficient Authorization'}
                    return message, 401
            except:
                message = {'Error':'Improper Access Method'}
                return message, 401
        else:
            message = {'Error':'No Bearer Token Provided'}
            return message, 401
    return decorated