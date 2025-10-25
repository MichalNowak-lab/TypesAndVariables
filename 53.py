###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
bottom = a*b
top = bottom
front = a*c
back = front
r_side = b*c
l_side = r_side
volume = a*b*c
surface_area = bottom+top+front+back+r_side+l_side
print(f'volume {volume}, surface area {surface_area}')
