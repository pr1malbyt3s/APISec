from . import db

class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
