w = float(input("Enter the width of the cheese:"))
h = float(input("Enter the height of the cheese:"))

areawhole= w * h

c1= float(input("Enter the diameter of circle 1 in the cheese:"))
c2= float(input("Enter the diameter of circle 2 in the cheese:"))

areac1 = (3.14 * c1**2)/4
areac2 = (3.14 * c2**2)/4

areatom= (areawhole - areac1 - areac2)/2

print("The area of cheese Tom should have is :",areatom)