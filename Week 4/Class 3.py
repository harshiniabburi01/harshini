sum = 0

#Input
for i in 1,2,3,4,5:
    x = int(input("Enter the value="))
    sum = sum + x

print("Sum =", sum)

#Checking for odd or even
if sum % 2 == 0:
    print("The sum of the numbers is even")
else:
    print("The sum of the numbers is odd")