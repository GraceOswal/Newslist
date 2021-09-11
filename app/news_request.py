import requests

from config import Config

class NewsRequest:
    def __init__(self):

        self.API_KEY = Config.API_KEY

    def get_sources(self):

        sources = []
        sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(sources, self.API_KEY)
        response = requests.get(sources_url)
        if response.status_code == 