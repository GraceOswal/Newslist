from flask import render_template, request

from . import main
from ..import news_request as request

from urllib.request import Request


#Views
@main.route('/')
def index():
    sources = request.get_sources()
    
    return render_template('index.html', sources=sources)

@main.route('/articles', methods=["POST","GET"])
def articles_page():
    if request == 'POST':
        search = request.form.get("search")
        articles = request.get_articles(search)

    return render_template('articles.html')

@main.route('/article/<id>')
def source_article(id):
    source_articles = request.get_article_by_source(id)
    source = id
    return render_template('articles_show.html', source_articles=source_articles, source=source)