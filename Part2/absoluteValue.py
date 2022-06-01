"""Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/x+y ."""
def calculate_absolute_value(x, y):
    numerator = (x-y)*-1 # -1 is to calculate_absolute_valueby removing the negative sign
    denominator =  x+y
    result = numerator/denominator
    return result

print(calculate_absolute_value(3, 7))
    