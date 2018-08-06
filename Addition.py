#Chapter 4
'''
(Game: learn addition) Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise. The program is similar to Listing 4.1.
'''

import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

guess = eval(input(str(num1) + " + " + str(num2) + " = "))

answer = num1 + num2 

if guess == answer:
    print("Your answer is correct.")
else:
    print("Your answer is incorrect.")
