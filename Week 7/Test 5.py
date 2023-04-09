#creating function to calculate distance between two points
def distance(a1, b1, a2, b2):
    """
    input = a1, b1, a2, b2
    output = to calculate the distance between two points
    note = if input is a and b, the distance being calculated is AB. if b and 
c, BC and so on.
    """
    AB = (((b1 - a1)**2) + ((b2 - a2)**2))**(1/2)
    return AB
#input a, b and c
a1 = float(input("Enter x coordinate of A (a1): "))
a2 = float(input("Enter y coordinate of A (a2): "))
b1 = float(input("Enter x coordinate of B (b1): "))
b2 = float(input("Enter y coordinate of B (b2): "))
c1 = float(input("Enter x coordinate of C (c1): "))
c2 = float(input("Enter y coordinate of C (c2): "))

AB = distance(a1, b1, a2, b2) ** 2
BC = distance(b1, c1, b2, c2) ** 2
AC = distance(a1, c1, a2, c2) ** 2

#determining whether or not A, B and C can form a square triangle and printing output accordingly

if AB + BC == AC or AB + AC == BC or BC + AC == AB:
    print("A, B and C can form a square triangle")
else:
    print("A, B and C cannot form a square triangle")