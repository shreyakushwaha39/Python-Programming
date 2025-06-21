a="aeiouAEIOU"
str1=input("Enter a string:")
count=0
for i in str1:
    if(i in a):
        count+=1
print("Number of vowel in given strin is",count)       