def input_list():
    n = int(input("Enter the number of items: "))
    lst = []
    for i in range(n):
        x = int(input("Enter a number: "))
        lst.append(x)
    return lst
def increase():

    sum = 0
    count = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            lst[i] = lst[i] + 5
#########################

lst = input_list()

print("List = ", lst)
increase()

print("List = ", lst)