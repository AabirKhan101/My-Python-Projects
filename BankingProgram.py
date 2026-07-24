# Banking Program

def present_balance(balance):
    print(f"Your current balance is €{balance:.2f}")
    
def deposit_cash():
    amount = float(input("Enter the amount of cash you want to deposit: "))

    if amount < 0:
        print("You can't deposit a negative number")
        return 0
    else:
        return amount

def withdrawl(balance):
    amount = float(input("Enter the amount you want to withdrawl: "))

    if amount > balance:
        print("The withdrawl amount exceeds your balance")
        return 0
    elif amount < 0:
        print("You can not withdraw a negative number")
        return 0
    else:
        return amount
def main():
    balance = 0

    while True:
        print("---Pakistan State Bank ATM---")
        print("1.SHOW BALANCE")
        print("2.DEPOSIT")
        print("3.WITHDRAW")
        print("4.EXIT")

        decesion = input("Enter what you want to do (1-4): ")

        if decesion == "1":
            present_balance(balance)
        elif decesion == "2":
            balance += deposit_cash()
        elif decesion == "3":
            balance -= withdrawl(balance)
        elif decesion == "4":
            break
    

if __name__ == '__main__':
    main()