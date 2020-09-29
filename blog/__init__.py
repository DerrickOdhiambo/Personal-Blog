import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_name):
  #initializing app
  app = Flask(__name__)

  #application configurations
  app.config.from_object(config_options[config_name])

  from .request import configure_request
  configure_request(app)

  #initializing extensions
  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  #registering a blueprint
  from .main import main as main_blueprint
  from .users import users as users_blueprint
  from .posts import posts as posts_blueprint

  app.register_blueprint(main_blueprint)
  app.register_blueprint(users_blueprint)
  app.register_blueprint(posts_blueprint)

  return app