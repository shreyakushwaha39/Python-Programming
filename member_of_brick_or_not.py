#wap to define the list of BRICKS COUNTRIES and then check whether the country entered by user is member of BRICKS or not
#BRICKS: Brazil,Russia,India,China,South Africa
BRICKS=['Brazil','Russia','India','China','South Africa']
country=input("Enter the country name:")
if country in BRICKS:
    print(country,'is a member of BRICKS')
else:
    print(country,'is not a member of BRICKS')
