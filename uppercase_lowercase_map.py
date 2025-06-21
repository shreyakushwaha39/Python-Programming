#wap that convert string of all uppercase characters into string of all lowercase characters using map function
s="HELLO WORLD"
a=list(map(lambda x:x.lower(),s))
print("".join(a))