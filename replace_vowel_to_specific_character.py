str1=input("Enter a string:")
for i in str1:
    if(i in "aeiouAEIOU"):
        str1=str1.replace(i,"#")
print(str1)
    