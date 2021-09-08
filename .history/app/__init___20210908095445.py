
from flask import Flask
from .config import DevConfig

#Inializing application
app = Flask(__name__)

#This sets up configurations

from app import app