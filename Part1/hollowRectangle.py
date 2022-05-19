"""8. Print hollow rectangle of stars *"""
width = int(input("Input width of rectangle: "))
height = int(input("Input height of rectangle: "))
for i in range(1, height+1):
    if (i == 1 or i == height ):
        print('*'*width)
    else:
        print('*' + ' '*(width -2) + '*')