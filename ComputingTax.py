#Chapter 4: Compute Tax (

import sys

status = eval(input("Enter your filing status:\n0: single\
                    \n1: married jointly\n2: married seperately\
                    \n3: head of the household \n"))

income = eval(input("Enter your taxable income: \n"))

tax = 0

if status == 0:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 82250) * 0.25
    elif income <= 175050:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 +\
              (income - 82250) * 0.28
    elif income <= 372950: #needs to be fixed
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 +\
              (175050 - 82250) * 0.28 + (372950 - 175050) * 0.33 +\
              (income - 372950) * 0.35;
    else:
        income <= 372950: #needs to be fixed
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 +\
              (175050 - 82250) * 0.28 + (372950 - 175050) * 0.33 +\
              (income - 372950) * 0.35;
            
elif status == 1:
    print("Status is 1")
elif status == 2:
    print("Status is 2")
elif status == 3:
    print("Status is 3")
else:
    print("Invalid status")
    sys.exit()

print("Tax is", format(tax, ".2f"))
    
