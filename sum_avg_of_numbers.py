# Write a program to find the sum and average of n numbers using for loop.
n=int(input("Enter a number :"))
s=0
for i in range(1,n+1):
    s+=i
print("sum of ",n,"numbers: ",s)
print("average of",n,"numbers:",s/n)

