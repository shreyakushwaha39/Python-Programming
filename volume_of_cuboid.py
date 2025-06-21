#wap to find volume of cuboid using function
def cuboid_volume(l, b, h):
    return l * b * h

l = int(input("Enter the length of the cuboid: "))
b = int(input("Enter the breadth of the cuboid: "))
h = int(input("Enter the height of the cuboid: "))
volume = cuboid_volume(l, b, h)
print("The volume of the cuboid is:", volume)