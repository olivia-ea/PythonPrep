#Chapter 4: Conditionals
'''
Write a program that prompts the user to enter an integer and
checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
one of them (but not both). Here is a sample run:
'''

num = eval(input("Enter a number: "))

if num % 5 == 0 and num % 6 == 0:
    print(str(num) + " is divisible by 5 and 6.")
elif num % 5 == 0 or num % 6 == 0:
    if num % 5 == 0 and num % 6 != 0:
        print(str(num) + " is divisible by 5 but not by 6.")
    elif num % 5 != 0 and num % 6 == 0:
        print(str(num) + " is divisible by 6 but not by 5.")
else:
    print(str(num) + " is not divisible by 5 and not divisible by 6.")
