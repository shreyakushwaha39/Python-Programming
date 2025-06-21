#wap to remove all duplicate elements from the list
l=[1,2,3,4,5,1,2,3,4,5]
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)