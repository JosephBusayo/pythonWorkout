"""10. Print upside down right angle triangle of stars """
height = int(input("Enter height of traingle: "))
for i in range(height, 0, -1):
    print('*'*(i))
    