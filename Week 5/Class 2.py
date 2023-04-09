#Input
N = int(input("Enter the number of numbers="))

count = 0
sum = 0

#Average Calcultion
for i in range (1,N+1,1):
    x = int(input("Enter the value of the number="))
    if x % 2 == 0:
        count = count + 1
        sum = sum + x

#Output
if count == 0:
    print("There are no even numbers")
else:
    average = sum / count
    print("Average =", average)
