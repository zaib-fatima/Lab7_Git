# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")

# Ask the user to choose a conversion
choice = input("Choose conversion (1: Fahrenheit, 2: Kelvin): ")

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32



# Convert to Kelvin
kelvin = celsius + 273.15


# Choose which conversion result to show
choice = input("Enter 1 for Fahrenheit or 2 for Kelvin: ")

if choice == "1":
    print("Fahrenheit:", fahrenheit)
elif choice == "2":
    print("Kelvin:", kelvin)


