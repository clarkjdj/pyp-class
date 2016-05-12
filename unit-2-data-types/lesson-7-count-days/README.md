Write a function that receives two `date` objects, and returns the amount of days that have past from one date to the other. Make sure to check that the second date is greater than the first one.

Examples:

```
>>> count_days(date(2015, 1, 1), date(2016, 1, 1))
365
>>> count_days(date(2016, 1, 1), date(2015, 1, 1))
ValueError: Second date must be greater than first one.
```
