##Write a Python program to listify the list of given strings individually using
##Python map.
s="What is your language and your culture"
a=s.split()
listify=list(map(lambda x: [x],a))
print(listify)
