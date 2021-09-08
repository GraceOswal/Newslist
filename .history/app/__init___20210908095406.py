
from flask import Flask
from .config import Dev

#Inializing application
app = Flask(__name__)

from app import app