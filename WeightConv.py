# Weightconverter program

weight = float(input("Enter your weight:"))
unit = input("What is the unit of your weight (Kg or Lbs):").lower()

if unit == "kg":
    weight *= 2.205
    print(f"Your  weight in pounds is {round(weight, 2)} lbs")

elif unit == "lbs":
    weight /= 2.205
    print(f"Your weight in kilograms is {round(weight)} kg")

else:
    print(f"{unit} is either not a valid unit or it is not measured in this calculator")
