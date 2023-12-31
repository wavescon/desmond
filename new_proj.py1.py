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

# Get user input for Fahrenheit temperature
try:
    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Convert Fahrenheit to Celsius
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Display the result
print(f"{fahrenheit_temperature:.2f} Fahrenheit is equal to {celsius_temperature:.2f} Celsius.")
