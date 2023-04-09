#Input

employers = int(input("Enter the number of employers="))

#Total Tax Calculations

totaltax = 0

for i in range (1,employers+1,1):
    hours = int(input("Enter the number of hours worked"))
    pay = int(input("Enter the pay rate per hour="))
    salary = hours * pay
    if salary < 1000:
        tax = salary * 0.1
    else:
        tax = salary * 0.2

    totaltax = totaltax + tax

#Output
print("The total tax is=",totaltax)