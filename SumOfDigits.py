#Chapter 2: Sum the Digits

number = eval(input("Enter a 5 digit number: "))

digit1 = number // 10000 #gives you first digit

random1 = number % 10000

digit2 = random1 // 1000 #gives you second digit

random2 = random1 % 1000

digit3 = random2 // 100 #gives you third digit

random3 = random2 % 100

digit4 = random3 // 10 #gives you fourth digit

digit5 = random3 % 10 #gives you last digit

sum = digit1 + digit2 + digit3 + digit4 + digit5

print("The sum of", number, "is: ", sum)
