#Chapter 4: Number Guess

import random

num = random.randint(0, 101)

print("Guess a number between 1 to 100\n")

guess = -1
while guess != num:
    guess = eval(input("Guess: "))

    if guess == num:
        print(str(num) + " is correct!")
    elif guess > num:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
