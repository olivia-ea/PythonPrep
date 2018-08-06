#Chapter 5: Trig Functions

import math

print("Degree\t\tSin\t\tCos")

for i in range(0, 370, 10):
    print(i, "\t\t", format(math.sin(i), ".4f"), "\t",format(math.cos(i), ".4f"))
