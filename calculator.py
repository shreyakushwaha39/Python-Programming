# Description: This program is a simple calculator that takes two numbers and an operation as input and returns the result of the operation.
# The operation can be addition, subtraction, multiplication, or division.
a=int(input("num1:"))
b=int(input("num2:"))
c=input("Enter operation(+,-,/,*)")
if (c=="+"):
    print("sum: ",a+b)
elif (c=="-"):
    print("subtraction: ",a-b)
elif (c=="*"):
    print("multiplication: ",a*b)
elif (c=="/"):
    if(b!=0):
        print("Division: ",a/b)
    else:
        print("undefined!!")
else:
    print("invalid entry!!!")