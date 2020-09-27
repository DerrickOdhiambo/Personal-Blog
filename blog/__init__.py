from flask import Flask
from config import config_options

def create_app(config_name):
  #initializing app
  app = Flask(__name__)

  #application configurations
  app.config.from_object(config_options[config_name])

  #registering a blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app