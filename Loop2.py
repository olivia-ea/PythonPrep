#Loop 2

i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end = ' ')
    print("***")
    i += 1

'''
OUTPUT:
***
***
2 ***
3 2 ***
4 3 2 ***
'''
