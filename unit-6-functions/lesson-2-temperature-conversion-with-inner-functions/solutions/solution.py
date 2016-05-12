def convert_temperature(temperature, to='celsius'):
    def to_fahrenheit():
        return (temperature * 9 / 5) + 32

    def to_celsius():
        return (temperature - 32) * 5 / 9

    return (to_celsius if to == 'celsius' else to_fahrenheit)()
