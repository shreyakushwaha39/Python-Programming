str1=input("Enter a first string :")
str2=input("Enter a second string :")
flag=0
for i in str1:
    if i not in str2:
        flag=1
for j in str2:
    if j not in str1:
        flag=1
if(flag==0):
    print("given string are anagrams")
else:
    print("given string are not anagrams")
    
        


