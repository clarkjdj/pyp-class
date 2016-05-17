import unittest


class OOPTestCase(unittest.TestCase):
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

    def test_search_books_by_title(self):
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

        results = store.search_books(title='raven')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], raven)

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

        results = store.search_books(author='doyle')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], study_in_scarlet)

    def test_search_without_title_or_author_raises_error(self):
        store = BookStore()
        with self.assertRaises(AttributeError):
            store.search_books()


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
