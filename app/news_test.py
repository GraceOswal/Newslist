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
        self.new_news = News('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',
                            'https://abcnews.go.com', 'general', 'en-us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()