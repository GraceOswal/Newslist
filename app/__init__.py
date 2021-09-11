
from flask import Flask
from .config import DevConfig

#Inializing application
app = Flask(__name__, instance_relative_config = True)

#This sets up configurations
app.config.from_object(DevConfig)

app.config.from_pyfile('instance/config.py')

from app import views

from app import error