# Shopping Cart Program

items = []
prices = []

while True:
    item = input("Enter the item that you want to buy (e to exit): ")
    if item.lower() == "e":
        break
    else:
        price = float(input("Enter the price of the item: "))
        items.append(item)
        prices.append(price)


print("----- Your Receipt -----")
for item in items:
    print(item)
for price in prices:
    print(price)

print("The total price is :", sum(prices))