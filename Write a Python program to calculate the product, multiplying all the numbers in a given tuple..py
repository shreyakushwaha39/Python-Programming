##Write a Python program to calculate the product, multiplying all the
##numbers in a given tuple.
##Original Tuple:
##(4, 3, 2, 2, -1, 18)
##Product - multiplying all the numbers of the said tuple: -864
##Original Tuple:
##(2, 4, 8, 8, 3, 2, 9)
##Product - multiplying all the numbers of the said tuple: 27648
t=(3,4,5,6,1)
print(t)
prod=1
for i in t:
    prod*=i
print("Product - multiplying all the numbers of the said tuple:",prod)
