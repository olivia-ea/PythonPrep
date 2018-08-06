#Chapter 4: 2 Way If Else Statement

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

if num1 < num2:
    num1, num2 = num2, num1 #switches num1 to num2 and num2 to num1 if necessary

answer = eval(input("What is " + str(num1) + " - " + str(num2) + "?\n"))

if num1 - num2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", num1, "-", num2, "=", num1-num2, "." )
