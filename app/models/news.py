'''Model class for news app'''
class News:

    def __init__(self,source,title,description,urlimage,urltonews,category,language):
        self.source = source
        self.title = title
        self.description = description
        self.urltoimage = 'https://github.com/GraceOswal/Newslist/blob/master/abc%20image%201/img1.jpeg'/+poster
        self.urltonews = urltonews
        self.category = category
        self.language = language

'''model class for the article inheriting news'''

class Articles(News):
    def __init__(self):
        super(News, self).__init__()