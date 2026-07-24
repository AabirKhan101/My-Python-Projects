# Dice rolling program using ASCII Art
import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),
     
     5 : ("┌─────────┐",
          "│ ●     ● │",
          "│    ●    │",
          "│ ●     ● │",
          "└─────────┘"),
        
    6 :  ("┌─────────┐",
          "│ ●     ● │",
          "│ ●     ● │",
          "│ ●     ● │",
          "└─────────┘")
}

dice = []
roll_dice = int(input("Enter how many dice you want to roll?: "))
# total = 0

for die in range (roll_dice):
    dice.append(random.randint(1, 6))
print(dice)

# for die in range(roll_dice):
#     for line in dice_art.get(dice[die]):     # this code prints the dice vertically
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ") # this code prints the dice horizontally
    print()


total = sum(dice)

print(f"Your total is {total}")