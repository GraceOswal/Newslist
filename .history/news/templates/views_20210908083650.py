from flask import render_template
from news import 

#Views
@app.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    return render_template('/index.html')