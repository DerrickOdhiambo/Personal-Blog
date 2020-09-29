from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)
  comment = db.relationship('Comments', backref='user', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.profile_image}' )"


class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comment = db.relationship('Comments', backref='post', lazy=True)

  def __repr__(self):
    return f"User('{self.title}', '{self.date_posted}' )"


class Comments(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(20), unique=False, nullable=False)
  email = db.Column(db.String(100), unique=False, nullable=False)
  message = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  time_posted = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

  def __repr__(self):
    return f"User('{self.message}', {self.timestamp})"

class Quotes:

  def __init__(self,author,quote):
      self.author = author
      self.quote = quote


class Email(db.Model):
  __tablename__ = 'email'

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String, nullable=False, unique=True)
