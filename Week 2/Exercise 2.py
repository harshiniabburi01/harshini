x = float(input("Enter the width of the rectangle"))
y = float(input("Enter the height of the rectangle"))
r = float(input("Enter the radius of the circle"))

Acircle = 3.14 * (r**2)
Aboth = Acircle + (x * y)
weight = 3 * Aboth

print("Total weight of the objects",weight)


