#wap to find median of a list of number
l=[1,2,3,4,5,6,7,8,9]
l.sort()
if len(l)%2==0:
    m1=l[len(l)//2]
    m2=l[(len(l)//2)-1]
    m=(m1+m2)/2
else:
    m=l[len(l)//2]
print("Median of list is",m)
