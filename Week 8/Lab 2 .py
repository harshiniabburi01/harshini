def total_salary():
    sum = 0
    for item in lst_employers:
        age = item[1]
        salary = item[2]
        if age >= 25:
            sum = sum + salary
    return sum
def is_exist(name):
    p = -1
    for i in range(len(lst_employers)):
        item = lst_employers[i]
        item_name = item[0]

        if item_name == name:
            p = i
    return p

def increase_salary():
    name = input("Enter name: ")
    p = is_exist(name)
    if p == -1:
        print("Employer does not exist")
    else:
        salary = ...
        lst_employers[p][1] = lst_employers[p][2] * 1.2
        return lst_employers[p][2]

def highest_salary():
    maxsalary = 0
    maxname = lst_employers[2]
    for item in lst_employers:
        salary = item[2]
        name = item[0]
        if salary > maxsalary:
            maxsalary = salary
            maxname = name

    return maxname
##############################################
# List of employers [ [Name, Age, Salary] ]
lst_employers = [
    ["Tom", 25, 100],
    ["Jerry", 30, 200],
    ["Daisy", 20, 100],
    ["Marie", 20, 250]
]

print("Total salary = ", total_salary())
print("Exist = ", is_exist("Tom"))
increase_salary()
print(lst_employers)
print("Highest salary = ", highest_salary())