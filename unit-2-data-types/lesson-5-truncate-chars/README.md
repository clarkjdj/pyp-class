In the Django web framework, there's a helper called `truncatechars` that allows you to limit the length of a string to a given number of characters, and adds `...` prefix at the end of it.
You must write a Python function that mimics the same logic using String slicing.

Examples:

```
>>> truncatechars("This is so awesome", 4)
"This..."

>>> truncatechars("This is so awesome", 100)
"This is so awesome"

>>> truncatechars("This is so awesome", 0)
"..."

>>> truncatechars(True, 0)
ValueError
```
