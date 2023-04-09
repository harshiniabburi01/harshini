#Input
name = input("Enter your name:")
hours = float(input("Enter the number of hours worked:"))

#Salary Calculation

salary = hours * 10

if hours > 20:
    bonus = salary * 0.2
    if bonus > 50:
        b = 50
else:
    bonus = 0

finalsalary = salary + bonus

#Output
print(name,"Your final salary with bonus is:",finalsalary)

