# Calculator program
import math
operator = input("Select an operator (+, -, *, / etc):")
num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))

if operator == "+":   # addition
    print(num1 + num2)
elif operator == "-":  # subtraction
    print(num1 - num2)
elif operator == "*": # multiplication
    print(num1 * num2)
elif operator == "/": # division
    print(num1 / num2)
elif operator == "**": # exponentiation
    print(num1**num2)
elif operator == "square root of num1":
    print((num1)**0.5)
elif operator == "square root of num2":
    print((num2)**0.5)
elif operator == "modulus":
    print(abs(num1))
    print(abs(num2))
elif operator == "factorial":
    print(math.factorial(num1))
    print(math.factorial(num2))
else:
    print("Invalid operator")
