#Function to check area of rectangle
def check_rectangle_area (w,h):
    a = w * h

    if a >= 50:
        return True
    else:
        return False

#Number of rectnagles
n = int(input("Enter the number of rectangles="))

count = 0

#Inputs for the calculation of area
for i in range(n):
    w = float(input("Enter the width of the rectangle="))
    h = float(input("Enter the height of the rectangle="))

    g = check_rectangle_area(w,h)

    if g == True:
        count = count + 1

#Output
print ("Count = ", count)