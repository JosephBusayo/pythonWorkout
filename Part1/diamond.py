"""11. Print out a diamond"""
length = int(input("Enter length of diamond: "))
a=1
for i in range(1, length+1):
    print(' '*(length-i) + '*'*(a))
    a += 2
    if i == length:
        for i in range(length):
            print(' '*(i+1) + '*'*(a-4))
            a -=2