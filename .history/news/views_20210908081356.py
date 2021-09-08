from flask import render_template
from news import app

#Views
@app.route("/")
def index():