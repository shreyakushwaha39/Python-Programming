#wap to add corresponding elements of two lists using map function
l1=[2,3,4,5,6]
l2=[3,4,5,6,7]
l=list(map(lambda x,y: x+y,l1,l2))
print(l)
