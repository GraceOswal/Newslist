
from flask import Flask
from .config import Config

#Inializing application
app = Flask(__name__, instance_relative_config = True)

#This sets up configurations
app.config.from_object(Config)

app.config.from_pyfile('instance/config.py')

from app import views

from app import error