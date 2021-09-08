
from flask import Flask
from .config import DevConfig

#Inializing application
app = Flask(__name__)

#

from app import app