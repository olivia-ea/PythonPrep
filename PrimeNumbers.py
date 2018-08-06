#Chapter 5: Prime Factors

'''
(Find the factors of an integer) Write a program that reads an integer and displays
all its smallest factors, also known as prime factors. For example, if the input integer
is 120, the output should be as follows:
2 3 5 7 = prime numbers
'''

data = eval(input("Enter an integer: "))


if data % 2 == 0:
    print("Divisible by 2")

if data % 3 == 0:
    print("Divisible by 3")

if data % 5 == 0:
    print("Divisible by 5")

if data % 7 == 0:
    print("Divisible by 7")
