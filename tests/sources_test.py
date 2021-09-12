import unittest
from app.models import News


class Newstest(unittest.TestCase):
    '''
    This Test class is used to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        This Set up method will run before every Test
        '''
        self.new_source = News('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',
                            'https://github.com/GraceOswal/Newslist/blob/master/abc%20image%201/img1.jpeg', 'https://abcnews.go.com', 'general', 'en-us')

    def test_sources(self):
        self.assertTrue(isinstance(self.new_source,News))

if __name__ == '__main__':
    unittest.main()