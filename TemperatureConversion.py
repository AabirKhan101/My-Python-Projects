# Temperature conversion program
unit = input("what is the unit of your temperature (C or F):").upper()
temperature = float(input("Enter your temperature:"))

if unit == "C":
    temperature = round((temperature * 1.8) + 32, 1)
    print(f"Your temperature in Fahrenheit is {temperature}° F")
elif unit == "F":
    temperature = round((temperature / 1.8) + 32, 1)
    print(f"Your temperature in Celsius is {temperature}° C")
else:
    print(f"{unit} is an invalid unit")


# Formulas :
# Celsius to Farenheight : F = (C * 9/5) + 32
# Farenheight to Celsius : C = (F - 32) * 5/9