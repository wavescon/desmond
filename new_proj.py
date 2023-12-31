def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    - float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# Example usage:
fahrenheit_temperature = 32
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is equal to {celsius_temperature:.2f} Celsius.")
