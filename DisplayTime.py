#Chapter 2: Display Time (using Numeric Data Types and Operators)

seconds = eval(input("Input a integer for seconds to convert: "))

hours = seconds // 3600 

minutes = seconds % 3600

remainingMinutes =  minutes // 60

remainingSeconds = minutes % 60

print("The converted time", seconds, "seconds is: ", hours, "hours", remainingMinutes,
      "minutes and ", remainingSeconds, "seconds.")
