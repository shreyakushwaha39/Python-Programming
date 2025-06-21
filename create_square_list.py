#wap using filter function to a list of squares of number from 1 to 10. 
# then use the 4 statement in construct to sum of elements of the list
l=[x**2 for x in range(1,11)]
print(l)
l1=list(filter(lambda x:x%2==0,l))
print(l1)
print('sum of elements:',sum(l1))
