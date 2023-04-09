#Input
N = int(input("Enter the number of rings ="))

#Number of good rings calcution
count = 0

for i in range (1,N+1,1):
    radius = int(input("Enter the radius of the circle"))
    area = 3.14 * radius * radius

    if area >= 99:
        count = count + 1

#Output

print("The number of good rings Marie has is=",count)