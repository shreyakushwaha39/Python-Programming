#wap to print absolute value,square root and cube of a number by using math module
import math
def cube(n):
    return n**3
a=int(input("Enter a number:"))
print('absoulute value:',abs(a))
print('square root value:',math.sqrt(a))
print('cube of a number:',cube(a))

