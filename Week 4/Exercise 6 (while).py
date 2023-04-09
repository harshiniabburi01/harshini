#Input

employers = int(input("Enter the number of employers="))

#Total Salary Calculation

totalsalary = 0

i = 1
while i <= employers:
    hours = int(input("Enter the number of hours worked"))
    pay = int(input("Enter the pay rate per hour="))
    salary = hours * pay
    totalsalary = totalsalary + salary
    i = i + 1

#Output

print("The total salary is=",totalsalary)
