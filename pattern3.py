"""
A
A B
A B C 
A B C D
"""
n=int(input("enter a number:"))
for i in range(0,n):
    s=65
    for j in range(0,i+1):
        print(chr(s),end=' ')
        s+=1
    print("\n")