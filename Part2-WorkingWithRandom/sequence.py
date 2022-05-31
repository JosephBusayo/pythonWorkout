from random import randint, random

"""1. Generate 50 random numbers such that the 1st number is btwn 1 and 2,
the 2nd is btwn 1 and 3, the 3rd is btwn 1 and 4, . . . , and the last is btwn
1 and 51"""
num = 2
for i in range(50):
    print(randint(1, num), end=' ')
    num+=1
print("\n")
