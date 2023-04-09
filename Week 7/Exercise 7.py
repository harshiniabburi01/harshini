#Function for staircase
def staircase(s):
    for i in range(s):
        for j in range(i+1):
            print("*", end = " ")
        print()

#Input
a = int(input("Enter the value of a ="))
b = int(input("Enter the value of b = "))

#Output
for k in range(a):
    staircase(b)