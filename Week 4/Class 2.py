#Input the value of N

N = int(input("Enter a value for Total Number of Values ="))

#Sum of odd numbers calcultions

sum = 0

i = 1
while i <= N:
    x = int(input("Enter the values of the numbers:"))
    if x % 2 == 1:
        sum = sum + x
    i = i + 1
else:
    print("There are no odd numbers")

#The output
    print ("Sum of odd numbers =", sum )