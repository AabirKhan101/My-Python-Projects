# Compound Interest Calculator
principle = 0
rate = 0 
time = 0   # years

# The formula for Compound intereset is A = P(1 + r/100)**t

while True:
    principle = int(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be negative")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate can't be negative")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be negative")
    else:
        break


interest_calculation = principle * pow((1+rate/100), time)
print("---Calculation of interest---")
print(f"Principal amount is : ${principle}, rate is : {rate}%, time in years is : {time}yrs. The total interest amount will be after {time}yrs is : ${interest_calculation}")