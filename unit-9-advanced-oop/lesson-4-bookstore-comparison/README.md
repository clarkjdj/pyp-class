Extend your previous BookStore to include comparison methods.

Two authors are the same if their name and nationality are the same:

```python
a1 = Author(name="Edgar Allan Poe", nationality="American")
a2 = Author(name="Edgar Allan Poe", nationality="American")
assert a1 == a2
```

Two books are the same if their title and author are the same:

```python
poe = Author(name="Edgar Allan Poe", nationality="American")
b1 = Book(title="The Raven", author=poe)
b2 = Book(title="The Raven", author=poe)
assert b1 == b2
```
