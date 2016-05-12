Write a function `string2number(a_string)`, that converts given String into either an Integer or a Float depending on which of them is possible.

Example:

```
>>> string2number('2.8')
2.8  # float

>>> string2number('2')
2  # integer

>>> string2number('something-else')
ValueError  # not a valid number string

>>> string2number(False)
ValueError  # param must be a string
```
