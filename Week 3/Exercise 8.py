#Input
name = input("Enter the name of the employer=")
salary = float(input("Enter the salary of the employer = "))

#Tax Calculation
if salary <= 1000:
    tax = salary * 0.1

elif 1000 < salary < 2000:
    tax = salary * 0.2

elif 2000 < salary < 3000:
    tax = salary * 0.3

else:
    tax = salary * 0.4

#Output

print("Name of Employer =",name,"Salary =",salary,"Tax=",tax)