#Chapter 5: Compute Tuition

'''
(Financial application: compute future tuition) Suppose that the tuition for a university
is $10,000 this year and increases 5% every year. Write a program that
computes the tuition in ten years and the total cost of four years’ worth of tuition
starting ten years from now.
'''

print("Current tuition: $ 10,000\n")

tuition = 10000
for i in range(1, 11):
    tuition = (tuition * 0.05) + tuition
    i += 1

print("Tuition after ten years: $",format(tuition, ".2f"))

tuition4 = tuition

for i in range(1, 5):
    tuition4 = (tuition4 * 0.05) + tuition4
    i += 1

print("\nTuition after fourteen years: $",format(tuition4, ".2f"))
print("\tTuition in the four year period: $", format((tuition4 - tuition), ".2f"))
    

