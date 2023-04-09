#Calcualtion of average of all numbers divsible by 7

sum = 0
average = 0
count = 0

for i in range (10,99):
    if i % 7 == 0:
        sum = sum + i
        count = count + 1
        average = sum / count

print("The average of the numbers is =",average)
