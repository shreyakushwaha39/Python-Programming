##Write a Python program to add two given lists and find the difference
##between them. Use the map() function.
l1=[4,5,6,7,8,9]
l2=[8,9,0,6,7,4]
add=list(map(lambda x,y: x+y,l1,l2))
diff=list(map(lambda x,y: x-y,l1,l2))
print(add)
print(diff)
