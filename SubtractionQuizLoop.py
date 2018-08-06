#Chapter 5: Repeat Subtraction Quiz

import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

if num1 < num2:
    num1, num2 = num2, num1

guess = eval(input(str(num1) + " - " + str(num2) + " = "))

answer = num1 - num2

while guess != answer:
    guess = eval(input(str(num1) + " - " + str(num2) + " = "))

print("That's correct!")
    

