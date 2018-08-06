#Chapter 3: Display Payroll

#User input and variable assignment 
name = input("Enter a name: ")
hours = eval(input("Enter the number of hours worked: "))
hourly = eval(input("Enter the hourly pay rate: "))
federal = eval(input("Enter the federal withholding rate: "))
state = eval(input("Enter the state withholding rate: "))

#Calculations

grossPay = hourly * hours
fedDeduct = (federal / 100) * grossPay
staDeduct = (state / 100) * grossPay
totDeduct = fedDeduct + staDeduct
netPay = grossPay - (fedDeduct + staDeduct)

#Print results
print("Employee Name: ", name, "\n\tHours Worked: ", hours,
      "hours\n\tPay Rate: $", format(hourly, ".2f"), "per hour\n\tGross Pay: $",
      format(grossPay, ".2f"), "\nDeductions: \n\tFederal Withholding: $",
      format(fedDeduct, ".2f"), "\n\tState Withholding: $",
      format(staDeduct, ".2f"), "\n\tTotal Deductions: $",
      format(totDeduct, ".2f"), "\nNet Pay: $", format(netPay, ".2f"))

