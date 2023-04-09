
#Calcualtion of average of all numbers divsible by 7

i = 10

sum = 0
avergae = 0
count = 0

while i <= 100:
    if i % 7 == 0:
        sum = sum + i
        count = count + 1
        average = sum / count
    i = i + 1

print("The average of the numbers is =", average)