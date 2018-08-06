#Chapter 3: Compute Change

money = eval(input("Enter a dollar and change amount: "))

remainingAmount = int(money * 100)

dollars = remainingAmount // 100

looseChange1 = remainingAmount % 100

quarters = looseChange1 // 25

looseChange2 = looseChange1 % 25

dimes = looseChange2 // 10

looseChange3 = looseChange2 % 10

nickels  = looseChange3 // 5

pennies = looseChange3 % 5

print(money, "converts to:", dollars, "dollars", quarters, "quarters",
      dimes, "dimes", nickels, "nickels", pennies, "pennies")
