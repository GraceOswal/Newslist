from config import Config
import urllib.request,json
from app.models import News, Articles
from urllib import request



api_key = None

#news base url
base_url=None

def configure_request(app):
    global api_key, base_url
    api_key ='2e763f47f2594cc791a0e476eaa77dcd'
    base_url = app.config['NEWS_API_URL_ALL']


def get_sources():

        sources = []
        sources_url = 'https://newsapi.org/v2/sources?q=tesla&apiKey={}'.format('d00a6496e549441e9d5edc3341b8a1bf')
        response = request.urlopen(sources_url)
        print(sources_url)
        if response.status == 'ok':
            for data in response.json()['sources']:
                sources.append(data)
        print(sources)
        return sources

def get_articles(self, article):
        articles = []
        articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(articles, self.api_key)
        response = request.get(articles_url)
        if response.status == 'ok':
            for data in response.json()['articles']:
                articles.append(data)
            print(articles)

        return articles

def get_article_by_source(self, id):
        source_articles = []
        source_articles_url = 'https://newsapi.org/v2/everything?sources={}?apiKey={}'.format(id, self.API_KEY)
        response = request.get(source_articles_url)
        if response.status== 'ok':
            for data in response.json()['articles']:
                source_articles.append(data)
            print(source_articles)
        return source_articles