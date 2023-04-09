#Function to check the area of rectnagles > 50
def check_rectangle_area (w,h):
    a = w * h

    if a >= 50:
        return True
    else:
        return False

#Function to calculate the area of the rectangles
def calculate_area(w,h):
    area = w * h
    return (area)

#Input for number of rectnagles
n = int(input("Enter the number of rectangles="))
sum = 0

#Input for height and width of rectangles
for i in range(n):
    w = float(input("Enter the width of the rectangle="))
    h = float(input("Enter the height of the rectangle="))
#Check and calculating the area of rectangles > 50

    if check_rectangle_area(w,h)==True:
        sum = sum + calculate_area(w,h)
#Output
print ("  Total Area of rectangles bigger than 50 = ", sum)