#Chapter 2: Split Digits (Reverse digits)

value = eval(input("Enter a four digit number: "))

digit1 = value // 1000

random1 = value % 1000

digit2 = random1 // 100

random2 = random1 % 100

digit3 = random2 // 10

digit4 = random2 % 10

print(value, "reversed is: ", digit4, digit3, digit2, digit1)
