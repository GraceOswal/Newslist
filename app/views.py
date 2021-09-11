from flask import render_template
from app import app, news_request
from .request import NewsRequest

#Views
@app.route('/')
def index():
    sources = news_request.get_sources()
    if sources:
        return render_template('index.html', sources=sources)

@app.route('/articles', methods=["POST","GET"])
def articles_page():
    if request.method == 'POST':
        search = request.form.get("search")
        articles = news_request.get_articles(search)
    else:
        articles = news_request.get_articles("verge")
    return render_template('articles.html',)