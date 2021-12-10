from app import app
from app.auth import basic_auth_required, jwt_token_required
from flask import json, jsonify, request



@app.route('/')
def home():
    message = {'message':'Welcome to the home endpoint!'}
    return jsonify(message)

@app.route('/basic_auth')
@basic_auth_required
def basic_auth():
    message = {'message':'Welcome to the basic_auth authenticated endpoint!'}
    return jsonify(message)

@app.route('/jwt_auth')
@jwt_token_required
def jwt_auth():
    message = {'message':'Welcome to the jwt_auth authenticated endpoint!'}
    return jsonify(message)