##Write a Python program to compute the element-wise sum of given tuples.
##Original lists:
##(1, 2, 3, 4)
##(3, 5, 2, 1)
##(2, 2, 3, 1)
##Element-wise sum of the said tuples:
##(6, 9, 8, 6)
print("Original lists:")
a=(1, 2, 3, 4)
b=(3, 5, 2, 1)
c=(2, 2, 3, 1)
suma=0
sumb=0
sumc=0
l=[]
for i in a:
    suma+=i
l.append(suma)
for i in b:
    sumb+=i
l.append(sumb)
for i in c:
    sumc+=i
l.append(sumc)
print("Element-wise sum of the said tuples:")
print(tuple(l))

