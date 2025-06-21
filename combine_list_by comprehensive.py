#wap to combine values in two list using list comprehension.
#combine only those value of alist that are multiple of values 
#in the first list.
l1=[1,2,3,4,5,6,7,8,9]
l2=[2,4,6,8,10,12,14,16,18]
l3=[i for i in l1 if i in l2]
print(l3)
