#Function to check the area of rectnagles > 50
def check_rectangle_area (w,h):
    a = w * h

    return a

#Input for number of rectnagles
n = int(input("Enter the number of rectangles="))
sum = 0

#Input for height and width of rectangles
for i in range(n):
    w = float(input("Enter the width of the rectangle = "))
    h = float(input("Enter the height of the rectangle = "))

#Check and calculating the area of rectangles > 50

    a = check_rectangle_area(w,h)

    if a > 50:
        sum = sum + a

#Output
print ("  Total Area of rectangles bigger than 50 = ", sum)