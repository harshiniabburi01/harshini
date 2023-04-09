# Check rectangle circumfrence
def check_rectangle_circumfrence(w,h):
    c = (w*2)+(h*2)

    if c > 50:
        return True
    else:
        return False
    return c

#Area of rectnagle
def rectangle_area(w,h):
    area = w * h
    return area

#Input
n = int(input("Enter the number of rectangles"))

area = 0
count = 0

#Confition and checking
for i in range (n):
    w = float(input("Enter the width of the rectangle="))
    h = float(input("Enter the height of the rectangle = "))

    g = check_rectangle_circumfrence(w,h)

    if g == True:
        area = area + rectangle_area(w,h)
        count = count + 1

average = area / count

#Output
print("The average area of rectangles of circumfrence bigger than 50 = ",average)