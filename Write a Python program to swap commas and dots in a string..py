##Write a Python program to swap commas and dots in a string.
##Sample string: "32.054,23" 
##Expected Output: "32,054.23"
s=input("Enter a string:")
s=s.replace('.','temp_dot').replace(',','temp_comma')
s=s.replace('temp_dot',',').replace('temp_comma','.')
print(s)
