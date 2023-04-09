#creating function to calculate equcaldoian distance between two points
from math import sqrt

def distance(a, b, xi , yi):
    """
    input = a , b , xi , yi
    output = to calculate the euclidean distance between two points
    note = if input is a and b, the distance being calculated is AB. if xi and
yi, xi,yi and so on.
    """
    d = sqrt((a - xi)**2) + ((b - yi)**2)
    return d

a = float(input("Enter the x co-ordinate of center A = "))
b = float(input("Enter the y co-ordinate of center A = "))
r = float(input("Enter the radius of cicrle C = "))

n = int(input("Enter the number of points Bi = "))

count = 0

for i in range (n):
    xi = float(input("Enter the value of the x co-ordinate = "))
    yi = float(input("Enter the value of the y co-ordinate = "))

    g = distance(a,b,xi,yi)

    if r >= g :
        count = count + 1

print("The number of points that lie inside the circle are = ",count)