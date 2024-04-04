from flask_login import UserMixin
from datetime import datetime
from .extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    posts = db.relationship('Post', backref='author', passive_deletes=True)
    likes = db.relationship('Like', backref='author', passive_deletes=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    
    created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    
    likes = db.relationship('Like', backref='post', passive_deletes=True)

    def __repr__(self):
        return f'<Post {self.title}>'

class Like(db.Model):
    __tablename__ = 'likes'
    
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f'<Like {self.id}>'