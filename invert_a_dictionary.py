#wap that invert the list of dictionary
a=['name','age','sport']
b=['Dev','19','cricket']
c=dict(zip(b,a))
d={key:value for value,key in c.items()}
print(c)
print(d)
