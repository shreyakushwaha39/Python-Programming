#wap to check whether a given year is a leap year or not
y=int(input('Enter a year:'))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("given year is a leap year")
        else:
            print("given year is not a leap year")
    else:
        print("given year is a leap year")
else:
    print("given year is not a leap year")