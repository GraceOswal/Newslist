from flask import render_template
from app import app

#Views
@app.route('/news/<news_id>')
def news(news_id):

    '''
    View the news page function that returns the details of news page
    and its data.
    '''

    return render_template('movie.html',  = message)