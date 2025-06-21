#wap to filter out string of length less than some specific value from the list using filter function
l=['Dev','krish','raj','kumar','ram','shyam']
n=int(input("Enter the length of string:"))
l=list(filter(lambda x: len(x)<=n,l))
print(l)
