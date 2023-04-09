#Input
N = int(input("Enter the value of N ="))

max = 0

i = 1
while N >= i:
    x = int(input("Enter a number="))
    if x > max:
        max = x
    i = i + 1

print("The biggest number is = ", max)

