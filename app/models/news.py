class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,poster,url,category,language):
        self.id = id
        self.title = title
        self.description = description
        self.poster = 'https://github.com/GraceOswal/Newslist/blob/master/abc%20image%201/img1.jpeg'/+poster
        self.url = url
        self.category = category
        self.language = language