#wap that a list of both positive and negative number,create another 
#list with filter function that only have positive number
l=[1,2,4,-2,3,-12,14,8,98,23,56]
a=sum(l)
print(a)
b=filter(lambda x:x>0,l)
print(list(b))
