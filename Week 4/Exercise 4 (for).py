#Input
N = int(input("Enter the number of numbers="))

max = 0

#Finding the biggest number
for i in range (N):
    x = int(input("Enter the value of the number= "))
    if x > max:
        max = x

#Output
print("The biggest number is =", max )