#Input

x1 = float(input("Enter the value of x1 ="))
y1 = float(input("Enter the value of y1="))
x2 = float(input("Enter the value of x2="))
y2= float(input("Enter the value of y2="))

#Manhattan Distance calculation

if x1 - x2 >= 0:
    x = (x1 - x2)
else:
    x = -(x1 - x2)

if y1 - y2 >= 0:
    y = (y1 - y2)
else:
    y = -(y1 - y2)

d = x + y

#Output

print("The Manhattan distance between the points is =",d)
