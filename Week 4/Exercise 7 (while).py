#Input

employers = int(input("Enter the number of employers="))

#Total Tax Calculations

totaltax = 0

i = 1
while i <= employers:
    hours = int(input("Enter the number of hours worked"))
    pay = int(input("Enter the pay rate per hour="))
    salary = hours * pay
    if salary < 1000:
        tax = salary * 0.1
    else:
        tax = salary * 0.2

    totaltax= totaltax + tax
    i = i + 1

#Output
print("The total tax is=",totaltax)
