# wap to create a list of number from 1-10 .
# then delete all the even number from the list and print the final list
l=[x for x in range(1,11)]
print(l)
l1=list(filter(lambda x:x%2!=0,l))
print(l1)