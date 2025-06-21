##Write a Python program to triple all numbers in a given list of integers.
##Use Python map.
l=[1,2,3,4,5,6,-4,-6,-7]
triple=list(map(lambda x: x**3,l))
print(triple)
