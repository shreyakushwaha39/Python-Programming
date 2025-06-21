#wap to filter out prime numbers from the list using filter function
l=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
l=list(filter(lambda x: all(x%i!=0 for i in range(2,x)),l))
print(l)
