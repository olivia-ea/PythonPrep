#Chapter 4: Generating Random Numbers

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

answer = eval(input("What is " + str(num1) + " + " + str(num2) + "?\n"))

print(num1, "+", num2, "=", answer, "which is", num1 + num2 == answer)
