name = input("Enter the name of the employer=")
hours = float(input("Enter the number of hours worked="))
salary = hours * 10

if hours > 20:
    salary = salary * 1.2

print("name:",name,"total salary:",salary)