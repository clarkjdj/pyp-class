Write a function that receives two `date` objects, and returns the amount of days that have past from one date to the other. The second date should be either greater or equal to the first date passed. If the second date is **smaller** than the first one, a `ValueError` should be raised.

Examples:

```python
>>> count_days(date(2015, 1, 1), date(2016, 1, 1))
365
>>> count_days(date(2016, 1, 1), date(2015, 1, 1))
ValueError: Second date must be greater than first one.
```
