Build a calculator using only static and class methods.

This is the way it should work:

```python
Calculator.add(2, 4)  # 6
Calculator.subtract(8, 1)  # 7
Calculator.multiply(3, 5)  # 15
Calculator.divide(5, 2)  # 2.5
```

Note that I've never created an instance of the calculator. I'm using the regular class.

One final addition. The `subtract` method **must** be implemented using the `add` method. Something like this:

```python
subtract = add(x, y * -1)
```
