#Chapter 6: Find Max

def max(num1, num2):
    if num1 > num2:
        result = num1
    if num2 > num1:
        result = num2
    return result

def main():
    i, j = eval(input("Enter two numbers: "))
    k = max(i, j)
    print("The largest number is: ", k)

main()
