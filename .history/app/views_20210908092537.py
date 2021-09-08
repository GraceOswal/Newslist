from flask import render_template
from app import app

#Views
@app.route('/news/<news_id>')
def news(news_id):

    '''
    View the news page function that returns the details of newspage and its data
    '''

    message = 'The News List'
    return render_template('index.html', message = message)