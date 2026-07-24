# DISCLAIMER : Betting is forbiden in Islam and is addicting. Betting causes moral corruption and is harmful to one's character, wealth and family. This is meant to make you realise how bad betting is. Thank you.

# Slot Machine Program
import random
import time
def spin_reel():
    symbols = ["🍒", "🍊", "7️⃣", "🔔", "⭐"]
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result

def show_reel(outcome):
    print("--------------")
    print(" | ".join(outcome))
    print("--------------")

def payment(outcome, bet):
    if outcome[0] == outcome[1] == outcome[2]:
        if outcome[0] == "🍒":
            return bet * 2
        elif outcome[0] == "🍊":
            return bet * 3
        elif outcome[0] == "⭐":
            return bet * 5
        elif outcome[0] == "🔔":
            return bet * 10
        elif outcome[0] == "7️⃣":
            return bet * 20
    return 0

def main():
    balance = 50

    print("====================")
    print("🎰 Welcome to Lucky Se7ven Casino")
    print("Symbols : 🍒 🍊 7️⃣  🔔 ⭐")
    print("====================")

    while balance > 0:
        
        print(f"Your balance amount is : £{balance}")

        bet = int(input("Enter the amount of bet that you will place: "))

        if bet > balance:
            print("You don't have that amount :/")
            continue
        
        if bet <= 0:
            print("Bet must be greater than zero")
            continue
        
        balance -= bet
        outcome = spin_reel()
        print("Spinning...\n")
        time.sleep(0.5)
        show_reel(outcome)

        payout = payment(outcome, bet)
        if payout > 0:
            print("YOU HAVE WON THE GAME!")
            print(f"YOUR PRIZE : {payout}")
            balance += payout
            print(f"Your new balance is : {balance}")
            break
        else:
            print("YOU LOST 😂. TRY AGAIN!")
    
    print("-----------")
    print("GAME OVER")
    print("-----------")


if __name__ == '__main__':
    main()