#wap to filter even numbers from the list using filter function
l=[2,3,4,5,6,7,8,9,10]
l=list(filter(lambda x: x%2==0,l))
print(l)
