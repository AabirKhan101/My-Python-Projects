# Concession Stand Program

menu = {"pizza" : 3,
        "schnitzel" : 3.50,
        "pretzel" : 4,
        "lemonade" : 3.50,
        "popcorn" : 2.50,
        "corn cob" : 3,
        "soda" : 2.50,
        "fries" : 3}
total = 0
cart = []

for item, key in menu.items():
    print(f"{item:10} : €{key:.2f}")

while True:
    buy = input("What would you like to eat(e to exit): ")
    if buy.lower() == "e":
        break
    elif menu.get(buy) is not None:
        cart.append(buy) 

print("----------YOUR CART----------")
for buy in cart:
    total += menu.get(buy)
    print(buy, end=" ")
print()
print(f"Your total is €{total:.2f}")