#Chapter 2: Using Console Input


value1 = eval(input("Enter a value: "))

area = value1 * value1 * 3.14

print("The area for the circle of the radius ", value1, "is ", area)

'''
When omitting eval, write like so:

string1 = input("Enter a value: ")
radius = eval(string1)

This will convert the user input string to a numerical value
'''

