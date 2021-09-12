
from flask import Flask

from config import Config

#Inializing application
def create_app():
    app = Flask(__name__)

#Blueprint configurations
    app.config.from_object(Config)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app