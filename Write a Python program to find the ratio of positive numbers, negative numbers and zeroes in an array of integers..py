##Write a Python program to find the ratio of positive numbers, negative
##numbers and zeroes in an array of integers.
arr=[6,7,8,9,-5,-1,-2,9,0,7,0]
pos=list(filter(lambda x: x>0,arr))
neg=list(filter(lambda x: x<0,arr))
zero=list(filter(lambda x: x==0,arr))
print(f"{len(pos)} : {len(neg)} : {len(zero)}")
