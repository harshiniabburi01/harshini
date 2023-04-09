import math

def check_perfect_square (b):
    root = math.sqrt(b)

    if int(root + 0.5) ** 2 == b:
        return True
    else:
        return False

a = int(input("Enter a minimum value = "))
b = int(input("Enter a maximum value "))

count = 0
sum = 0
average = 0

for i in range(a):
    for j in range(b):
        g = check_perfect_square(b)
        if g == True:
            count = count + 1
            sum = sum + a
            average = sum / count

print("The average of all square numbers is = ",average )