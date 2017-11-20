from sqlalchemy import Column, ForeignKey, Integer, String#pragma:no cover
from sqlalchemy import create_engine#pragma:no cover
from sqlalchemy.orm import relationship#pragma:no cover
from app import db#pragma:no cover


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(300))
    post_id = db.relationship('User', backref='posts',
                                 lazy='dynamic')
    
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        db.create_all()   #pragma:no cover

    def __repr__(self):
        return '{}'.format(self.first_name +' '+ self.last_name)
    
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(60), nullable=False, unique=True)
    image_url = db.Column(db.String(100), nullable=False, unique=True)
    user_id = db.relationship('User', backref='posts',
                                 lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    def __init__(self, name, description):
        self.name = name
        self.description = description
        db.create_all()#pragma:no cover
