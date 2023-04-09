#Input

r1 = float(input("Enter the radius of ring 1 ="))
r2 = float(input("Enter the radius of ring 2="))
r3 = float(input("Enter the radius of ring 3 ="))

#Area Calcualtion

arear1 = 3.14 * (r1**2)
arear2 = 3.14 * (r2**2)
arear3 = 3.14 * (r3**2)

#Weight calculation
weightr1 = arear1 * 2
weightr2 = arear2 * 2
weightr3 = arear3 * 2

#Max weight calculations

maxweight = weightr1

if maxweight < weightr2:
    maxweight = weightr2
if maxweight < weightr3:
    maxweight = weightr3

#Output
print("The weight of the heaviest ring is",maxweight)
