import requests

from config import Config

class NewsRequest:
    def __init__(self):

        self.API_KEY = Config.API_KEY

    def get_sources(self):

        sources = []
        sources_url = 