##Write a Python program to convert a given tuple of positive integers into
##an integer.
##Original tuple:
##(1, 2, 3)
##Convert the said tuple of positive integers into an integer:
##123
##Original tuple:
##(10, 20, 40, 5, 70)
##Convert the said tuple of positive integers into an integer:
##102040570
print("Original tuple:")
t=(1, 2, 3)
print(t)
print("Convert the said tuple of positive integers into an integer:")
s=''
for i in t:
    s+=str(i)
print(s)
    
