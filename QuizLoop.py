#Chapter 5: Quiz Loop

import random
import time

correctCount = 0
count = 0
NUM_OF_Q = 5

startTime = time.time()

while count < NUM_OF_Q:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    if num1 < num2:
        num1, num2 = num2, num1
    
    guess = eval(input("What is " + str(num1) + " - " + str(num2) + " = "))

                 
    if num1 - num2 == guess:
        print("You are correct!")
        correctCount += 1
    else:
        print("You are incorrect. " + str(num1) + " - " + str(num2) + " = " + str(num1-num2))

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print("The correct count is", correctCount, "out of", NUM_OF_Q,
      "\nTest time is", testTime, "seconds.")
