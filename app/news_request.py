from config import Config
import urllib.request,json
from app.models import News, Articles

from urllib import request

api_key = None

#news base url
base_url=None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['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']
    base_url = app.config ['NEWS_API_URL_ALL']


    def get_sources(self):

        sources = []
        sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, self.API_KEY)
        response = request.get(sources_url)
        if response.status_code == 200:
            for data in response.json()['sources']:
                sources.append(data)
        print(sources)
        return sources

    def get_articles(self, article):
        articles = []
        articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(articles, self.API_KEY)
        response = request.get(articles_url)
        if response.status_code == 200:
            for data in response.json()['articles']:
                articles.append(data)
            print(articles)

            return articles

    def get_article_by_source(self, id):
        source_articles = []
        source_articles_url = 'https://newsapi.org/v2/everything?sources={}?apiKey={}'.format(id, self.API_KEY)
        response = request.get(source_articles_url)
        if response.status_code == 200:
            for data in response.json()['articles']:
                source_article.append(data)
            print(source_article)
            return source_article