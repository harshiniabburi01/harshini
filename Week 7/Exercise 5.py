#Calculate bonus
def calculate_bonus (age,salary):
    if age <= 30:
        bonus = salary * 0.1
    elif age <= 40:
        bonus = salary * 0.2
    elif age <= 50:
        bonus = salary * 0.3
    else:
        bonus = salary * 0.4

    return bonus

#Input

n = int(input("Enter the number of employers = "))

bonus = 0

for i in range(n):
    age = int(input("Enter the employers age = "))
    salary = float(input("Enter the eployers salary = "))
    bonus = bonus + calculate_bonus(age,salary)


#Output
print("The total bonus is = ", bonus)