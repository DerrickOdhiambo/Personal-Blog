from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options


db = SQLAlchemy()

def create_app(config_name):
  #initializing app
  app = Flask(__name__)

  #application configurations
  app.config.from_object(config_options[config_name])

  #initializing extensions
  db.init_app(app)

  #registering a blueprint
  from .main import main as main_blueprint
  from .users import users as users_blueprint

  app.register_blueprint(main_blueprint)
  app.register_blueprint(users_blueprint)

  return app