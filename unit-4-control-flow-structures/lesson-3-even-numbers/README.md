Write a function that receives a list of Integer values as a param, and returns a filtered list containing only even numbers.

A second Integer param is given to be used as limit for the returned list of numbers.

Examples:

```python
>>> even_numbers([1,2,3,4,5,6,7,8,9], 3)
[2,4,6]
>>> even_numbers([1,2,3,4,5,6,7,8,9], 20)
[2,4,6,8]
>>> even_numbers([1,2,3,4,5,6,7,8,9], 1)
[2]
>>> even_numbers([1,2,3,4,5,6,7,8,9], 0)
[]
```

_Note: List comprehensions must not be used. Only loops and their related statements are allowed._
