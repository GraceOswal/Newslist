'''Model class for news app'''
class News:

    def __init__(self,source,title,description,urltoImage,author):
        self.source = source
        self.title = title
        self.description = description
        self.urltoImage = urltoImage
        self.author = author

'''model class for the article inheriting news'''

class Articles(News):
    def __init__(self):
        super(News, self).__init__()