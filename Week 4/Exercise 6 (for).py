#Input

employers = int(input("Enter the number of employers="))

#Total Salary Calculation

totalsalary = 0

for i in range (1,employers+1,1):
    hours = int(input("Enter the number of hours worked"))
    pay = int(input("Enter the pay rate per hour="))
    salary = hours * pay
    totalsalary = totalsalary + salary

#Output

print("The total salary is=",totalsalary)