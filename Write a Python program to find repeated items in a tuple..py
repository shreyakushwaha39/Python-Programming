#Write a Python program to find repeated items in a tuple.
t=(56,67,78,67,54,45,54,678,33)
d={}
for i in t:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]>1:
        print(i)
    
        
