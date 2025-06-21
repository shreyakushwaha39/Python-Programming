##Write a Python program to convert a tuple of string values to a tuple
##of integer values.
##Original tuple values:
##(('333', '33'), ('1416', '55'))
##New tuple values:
##((333, 33), (1416, 55))
print("Original Tuple values:")
t=(('333', '33'), ('1416', '55'))
print(t)
l=[]
for i in t:
    a=tuple(int(x) for x in i)
    l.append(a)
print(tuple(l))
