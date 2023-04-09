sum = 0

#Input and Sum calculation

i = 1
while i <= 5:
    x = int(input("Enter number:"))
    sum = sum + x
    i = i + 1

print("Sum of the numbers =",sum)

#Odd or even

if sum % 2 == 0:
    print("The sum is an even number")
else:
    print("The sum is an odd number")