##Write a Python program to convert all the characters into uppercase and
##lowercase and eliminate duplicate letters from a given sequence. Use the
##map() function.
s="This is the world."
upper=list(map(lambda x: x.upper(),dict.fromkeys(s)))
lower=list(map(lambda x: x.lower(),dict.fromkeys(s)))
print(" ".join(upper))
print(" ".join(lower))
