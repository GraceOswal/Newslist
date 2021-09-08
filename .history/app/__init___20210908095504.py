
from flask import Flask
from .config import DevConfig

#Inializing application
app = Flask(__name__)

#This sets up configurations
app.config.from_object(D)

from app import app