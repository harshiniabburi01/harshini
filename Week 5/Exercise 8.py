N = int(input("Enter the value of N = "))

sum = 0
count = 0

for i in range (N):
    name = input("Enter name =")
    salary = float(input("Enter the salary = "))
    gender = input("Enter the gender of employer = ")

    if salary < 1000:
        tax = salary * 0.1
    elif salary <= 2000:
        tax = salary * 0.2
    else:
        tax = salary * 0.3


    if gender == "female":
        sum = sum + tax
        count = count + 1

if count == 0:
     print("There are no female employers")
else:
    print("average =", sum/count)