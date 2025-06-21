##Write a Python program to convert a given list of integers and a tuple of
##integers in a list of strings.
l1=[9,0,-7,-6,-5,4,3,8,1]
l2=(7,9,6,4,3,-5,-3,-2,1)
l=list(l1)+list(l2)
string=list(map(lambda x: str(x),l))
print(string)
