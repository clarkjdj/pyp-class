Implement a simple bookstore using OOP.
The BookStore should implement a special `search_books` method.
This method should accept two optional parameters, either `title` to search
by book title or `author`, to search by author's name.

Example:

```python
store = BookStore()
# Authors
poe = Author(name="Edgar Allan Poe", nationality="American")
doyle = Author(name="Arthur Conan Doyle", nationality='British')

# Books
raven = Book(title="The Raven", author=poe)
study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

store.add_book(raven)
store.add_book(study_in_scarlet)

store.search_books(title='raven')  # [raven]
store.search_books(author='doyle')  # [study_in_scarlet]
```
