
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
        for book in self.books:
            if author.lower() in book.author.name.lower():
                yield book

    def search_books(self, title=None, author=None):
        if not any([title, author]):
            raise AttributeError("You must provide title or author")
        results = None
        if title:
            # Python>=3.3 syntax:
            # yield from self._search_title(title)
            results = self._search_title(title)
        if author:
            # Python>=3.3 syntax
            # yield from self._search_author(author)
            results = self._search_author(author)

        for result in results:
            yield result


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __eq__(self, other):
        return (self.name == other.name and
                self.nationality == other.nationality)


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return (self.title == other.title and
                self.author == other.author)
