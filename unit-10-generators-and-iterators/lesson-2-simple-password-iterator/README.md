Write a simple random password generator using iterators. The generator can accept two parameters:
* `available_chars`: The characters to use to generate the password. OPTIONAL. Default: A set of lowercase characters, digits and symbols. (hint, check the `string` module)
* `length`: The length of the password. OPTIONAL. Default: 8

```python
pass_generator = SimplePasswordGenerator()
next(pass_generator)  # %58a$d8a (length=8)

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
next(pass_generator)  # 'abba'
```

*Note: Make sure you implement the generator in a way that supports both Python2.7 and Python3*
