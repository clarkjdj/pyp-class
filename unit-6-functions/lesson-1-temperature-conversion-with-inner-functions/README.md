# Temperature conversion with inner functions

Write a function `convert_temperature` that receives two parameters, a number (indicating degrees of temperature) and an optional second parameter indicating if it should convert the temperature to Celsius or Fahrenheit (default is Celsius). The function should have two inner functions `to_celsius` and `to_fahrenheit` that receive NO parameters and must be used to return the expected result. Example:

```python
convert_temperature(32)  == 0  # celsius is default
convert_temperature(32, to='celsius')  == 0
convert_temperature(40, to='fahrenheit') == 104
```
