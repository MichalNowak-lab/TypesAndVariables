###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x # z takes x value, keeping it
x = y # swaps x value with y
y = z # y takes x value which was added to z before
print("After swapping: x=", x, "y=", y)