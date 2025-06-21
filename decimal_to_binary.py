#wap to convert a decimal number to binary number
n=int(input("Enter a decimal number:"))
bin=""
if(n==0):
    print("0")
while n>0:
    bin+=str(n%2)
    n//=2

print(bin[::-1])
