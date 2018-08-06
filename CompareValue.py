#Chapter 4: Comparing Value

'''
 Suppose you shop for rice and find it in two differentsized
packages. You would like to write a program to compare the costs of the
packages. The program prompts the user to enter the weight and price of each
package and then displays the one with the better price. Here is a sample run:
'''

w1, p1 = eval(input("Enter the weight and price for package 1: "))
w2, p2 = eval(input("Enter the weight and price for package 2: "))


value1 = p1/w1
value2 = p2/w1

if value1 > value2:
    print("Package 1 has better value.")
else:
    print("Package 2 has better value.")
