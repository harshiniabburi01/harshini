x1 = float(input("Enter the value of x1 :"))
y1 = float(input("Enter the value of y1 :"))
x2 = float(input("Enter the value of x2 :"))
y2 = float(input("Enter the value of y2:"))

AB2 =((x1-x2)**2) + ((y1-y2)**2)

r = AB2 ** 0.5
area = 3.14 * (r**2)

print ("The area of the circle is:",area)