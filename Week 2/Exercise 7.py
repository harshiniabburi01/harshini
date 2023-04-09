x1 = float(input("Enter the value of x1 :"))
y1 = float(input("Enter the value of y1 :"))
x2 = float(input("Enter the value of x2 :"))
y2 = float(input("Enter the value of y2:"))

w = x2 - x1
h = y2 - y1

area = w * h

circumfrence = (w*2)+(h*2)

print("The area of the rectangle created by point A and B is:",area)
print("The circumfrence of the rectangle created by point A and B is:", circumfrence)