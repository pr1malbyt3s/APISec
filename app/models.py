from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(64), nullable=False)
