from flask import render_template
from app import app

#Views
@app.route('/news/<int:news_id>')
def index():

    '''
    View the news page function that returns the details of news page
    and its data.
    '''
    title = 'Home - Welcome to our #1 Online News Blog, News at Your Doorstep!'
    return render_template('index.html', title = title)