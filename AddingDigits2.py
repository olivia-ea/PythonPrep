#Chapter 6: Adding Digits

'''
(Sum the digits in an integer) Write a function that computes the sum of the digits
in an integer. Use the following function header:
def sumDigits(n):
For example, sumDigits(234) returns 9 (Hint: Use the % operator
to extract digits, and the // operator to remove the extracted digit. For instance, to
extract 4 from 234, use 234 % 10 To remove 4 from 234, use 234 // 10
Use a loop to repeatedly extract and remove the digits until all the digits
are extracted.) Write a test program that prompts the user to enter an integer and
displays the sum of all its digits.
'''

def main():
    data = eval(input("Enter a three digit number: "))


def sumDigits(data):
    num1 = data // 100 #gives you first digit
    return num1
    mid = data % 100 #seperates to two last digits
    num2 = mid // 10 #gives you second digit
    return num2
    num3 = mid % 10 #gives you last digit
    return num3

    sumNum = num1 + num2 + num3
    return sumNum

       
main()

print("The sum of", sumDigits(num1), "+", sumDigits(num2), "+", sumDigits(num3), "=", sumDigits(sumNum))
