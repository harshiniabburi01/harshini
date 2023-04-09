def total_salary():
    sum = 0
    for i in range(len(lst_names)):
        salary = lst_salaries[i]
        age = lst_ages[i]
        if age >= 25:
            sum += salary
    return sum

def is_exist(name):
    p = -1
    for i in range(len(lst_names)):
        item_name = lst_names[i]
        if item_name == name:
            p = i
    return p

def increase_salary():
    name = input("Enter name: ")
    p = is_exist(name)
    if p == -1:
        print("Employer does not exist")
    else:
        salary = lst_salaries[p]
        lst_salaries[p] = lst_salaries[p] * 1.2


def highest_salary():
    maxsalary = lst_salaries[p]
    maxname = lst_names[i]

    for i in range(len(lst_names)):
        salary =
        name = lst_names[i]
        if lst_salaries > maxsalary:
            lst_salaries = maxsalary

    return maxname
##############################################

# List of names
lst_names = ["Tom", "Jerry", "Daisy", "Marie"]
# List of age
lst_ages = [25, 30, 20, 20]
# List of salaries
lst_salaries = [100, 200, 100, 250]
print("Total salary = ", total_salary())
print("Exist = ", is_exist("Tom"))
increase_salary()
print(lst_salaries)
print("Highest salary = ", highest_salary())