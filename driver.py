# TODO: Import the Temperature class from the temperature module

from temperature import Temperature

# Test the class:
# TODO: Create a temperature instance at 25°C
temp = Temperature(25)

# TODO: Print both Celsius and Fahrenheit values
# TODO: Use the format: "25.0°C is 77.0°F"

celsius_temp = temp.celsius
fahrenheit_temp = temp.fahrenheit

print(f"{celsius_temp}°C is {fahrenheit_temp}°F")

# TODO: Set the temperature to 98.6°F
temp.fahrenheit = 98.6
celsius_temp = temp.celsius
fahrenheit_temp = temp.fahrenheit

# TODO: Print both values again to confirm the conversion works
# TODO: Use the same format as before

print(f"{celsius_temp}°C is {fahrenheit_temp}°F")