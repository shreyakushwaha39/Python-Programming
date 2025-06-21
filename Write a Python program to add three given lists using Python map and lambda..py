##Write a Python program to add three given lists using Python map and lambda.
l1=[4,5,6,7,8,9,0]
l2=[8,9,0,6,4,7,8]
l3=[4,6,7,8,3,4,5,6]
add=list(map(lambda x,y,z: x+y+z,l1,l2,l3))
print(add)
