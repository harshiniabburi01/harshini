# List of employers [ [Name, Age, Salary] ]
lst = [
    ["Tom", 25, 100],
    ["Jerry", 30, 200],
    ["Daisy", 20, 100],
    ["Marie", 20, 250]
]


def is_exist(name):
    p = -1
    for i in range(len(lst)):
        item = lst[i]
        item_name = item[0]

        if item_name == name:
            p = i
    return p

