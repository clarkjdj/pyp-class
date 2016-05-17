import unittest


class BookStoreTestCase(unittest.TestCase):
    def test_class_relationships(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        self.assertEqual(store.books, [raven, study_in_scarlet])

        self.assertEqual(raven.author, poe)
        self.assertEqual(study_in_scarlet.author, doyle)


class ObjectsComparisonTestCase(unittest.TestCase):
    def test_compare_books(self):
        """Books with same author and title should be equal"""
        poe = Author(name="Edgar Allan Poe", nationality="American")

        b1 = Book(title="The Raven", author=poe)
        b2 = Book(title="The Raven", author=poe)
        self.assertEqual(b1, b2)

    def test_compare_authors(self):
        """Authors with same name and nationality should be equal"""
        a1 = Author(name="Edgar Allan Poe", nationality="American")
        a2 = Author(name="Edgar Allan Poe", nationality="American")

        self.assertEqual(a1, a2)


class BookGeneratorTestCase(unittest.TestCase):

    def test_search_books_by_title_returns_generator(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        results_generator = store.search_books(title='raven')
        self.assertEqual(next(results_generator), raven)
        with self.assertRaises(StopIteration):
            next(results_generator)

    def test_search_books_by_authors_name(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        results_generator = store.search_books(author='doyle')

        self.assertEqual(next(results_generator), study_in_scarlet)
        with self.assertRaises(StopIteration):
            next(results_generator)

    def test_search_without_title_or_author_raises_error(self):
        store = BookStore()
        with self.assertRaises(AttributeError):
            next(store.search_books())
