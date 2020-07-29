# -*- coding: utf-8 -*-
class BookViewModel(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = ' '.join(s for s in book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        res = ''
        for s in intros:
            if isinstance(s, list):
                s = ' '.join(s)
            res += ' | ' + s
        res = res.strip(' | ')

        return res


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

