## Write a Python program to check if a specified element appears in a
## tuple of tuples.
##Original list:
##(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
##Check if White present in said tuple of tuples!
##True
##Check if White present in said tuple of tuples!
##True
##Check if Olive present in said tuple of tuples!
##False
t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
color=input("")
found=False
for i in t:
    for x in i:
        if color in x:
            found=True
            break
print(found)

