r1 = float(input("Enter the radius of Ring 1:"))
r2 = float(input("Enter the radius of Ring 2:"))
r3 = float(input("Enter the radius of Ring 3:"))

area = (3.14 * (r1**2))+ (3.14 * (r2**2)) + (3.14 * (r3**2))

p = float(input("Enter the cost of each square meter:"))

cost = area * p

print("Overall value of Jerrys Rings:",cost)
