# quiz game

questions = ("What is the real name of the writer Geroge Orwell?",
             "Which animal is the largest mammal on Earth",
             "Which planet is known as the Red Planet?",
             "Which Pakistani PM has served the longest term in office?")

options = (("A. Eric Blair","B. Jackie Chan","C. Ricky Joe","D. Rusty Ryan"),
           ("A. Dog","B. Cat","C. Whale","D. Donkey"),
           ("A. Earth","B. Mars","C. Venus","D. Pluto"),
           ("A. Aabir Khan","B. Imran Khan","C. Liaquat Ali Khan","D. Nawaz Sharif"))
answers = ("A","C","B","D")
guesses = []
question_num = 0
score = 0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----RESULTS-----")

print("Correct Answers : ", end="")
for answer in answers:
    print(answer, end=" ")

print()

print("Your Answers : ", end="")
for guess in guesses:
    print(guess, end=" ")

print()

result = (score / len(questions))*100
print(f"Your score is : {result}%")