#convert list of temperature in celsius to fahrenheit
lc=[23,43,45,66,75]
fc=list(map(lambda c: (c*9/5)+32,lc))
print(fc)