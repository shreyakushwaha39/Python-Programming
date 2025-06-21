##Write a Python program to swap cases in a given string.
##Sample Output:
##pYTHON eXERCISES
##jAVA
##nUMpY
s=input("Enter a string:")
S=""
for i in s:
    if i.isupper():
        S+=i.lower()
    else:
        S+=i.upper()
print(S)
