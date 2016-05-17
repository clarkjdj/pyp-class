class BookStore(object):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def _search_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def _search_author(self, author):
        results = []
        for book in self.books:
            if author.lower() in book.author.name.lower():
                results.append(book)
        return results

    def search_books(self, title=None, author=None):
        if not any([title, author]):
            raise AttributeError("You must provide title or author")
        if title:
            return self._search_title(title)
        if author:
            return self._search_author(author)


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
