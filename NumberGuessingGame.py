# Number Guessing Game
import random

lowest_number = 1
highest_number = 100
gusses = 0
answer = random.randint(lowest_number, highest_number)

while True:
    guess = int(input(f"Guess a random number between {lowest_number} and {highest_number}: "))
    # if guess.isdigit():
    #     guess = int(guess)
    gusses += 1
    if guess < lowest_number or guess > highest_number:
        print(f"Invalid range. Please print in between {lowest_number} and {highest_number}")
    elif guess < answer:
        print("Too low, try again")
    elif guess > answer:
            print("Too high, try again")
    else:
        print(f"Correct answer, {answer} is the correct one!")
        print(f"The amount of guesses it took you is : {gusses}")
        break
    # else:
    #     print(f"Invalid guess, Please enter a digit in between {lowest_number} and {highest_number}.")