Convert the `search_books` method of the Bookstore class you implemented in the previous unit so it has an iterator-like interface.

Instead of returning a list with the results,
create a generator/iterator that behaves with the Iterator API:

```python
store = BookStore()
```

Both these pieces of code should work and be equivalent:

```python
# Using a for loop
results = store.search_books(title="raven")
for book in results:
    print(book)

# Invoking next directly
results = store.search_books(title="raven")
print(next(result))
print(next(result))
```
