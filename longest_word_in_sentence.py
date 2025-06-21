str1=input("enter a string:")
l1=str1.split(" ")
max=l1[0]
max1=0
for i in l1:
    count=len(i)
    if count>max1:
        max=i
print("Greatest word in given string is",max)
