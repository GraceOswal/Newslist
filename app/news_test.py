import unittest
from models import news
News = news.News

class Newstest(unittest.TestCase):
    '''
    This Test class is used to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        This Set up method will run before every Test
        '''
        self.new_news = News()