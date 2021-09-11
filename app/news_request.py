import requests

from config import Config

class NewsRequest:
    def __init__(self):

        self.API_KEY = Config.API_KEY

    def get_sources(self):

        sources = []
        sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, self.API_KEY)
        response = requests.get(sources_url)
        if response.status_code == 200:
            sources.append(data)
        print(sources)
        return sources

    def get_articles(self, article):
        article = []
    article_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(id, self.API_KEY)
    response = requests.get(articles_url)
    if response.status_code == 200:
        for data in response.json()['articles']
        articles.append(data)
    print(articles)
    return articles

    def get_article_by_source(self, id):
        source_articles = []
    source_articles_url = 'https://newsapi.org/v2/everything?sources={}?apiKey={}'.format(sources, self.API_KEY)
    response = requests.get(source_articles_url)
    if response.status_code == 200:
        source_articles.append(data)
    print(source_article)
    return source_article