#Chapter 2: Calculating Tips

subtotal, gratuity = eval(input("Enter the subtotal and gratuity values: "))

gratuityAmount = subtotal * (gratuity/100)

total = subtotal + gratuityAmount

print("The subtotal", subtotal, "and gratuity", gratuity, "% generate a total of",
      total, "with a gratuity of $", gratuityAmount)
