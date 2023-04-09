def sum_value():
    sum = 0
    for item in lst:
        price = item[1]
        quantity = item[2]
        value = price * quantity
        if price >= 3:
            sum += value
    return sum

def food_list():
    sub = []
    for item in lst:
        price = item[1]
        if price >= 3:
            sub.append(item[1])
        return sub

def update_food_price():
    name = input("Please input name = ")
    price = float(input("Please input price = "))

    in_list = False
    for i in range(len(lst)):
        item = lst[i]
        iname = item[0]
        if iname == name:
            in_list = True
            nitem = (item[0], price, item[2])
            lst_foods = nitem
            break
    if in_list == False:
        print("The food do not in the list")


lst = [("Apple", 5, 10), ("Banana", 2, 4), ("Grape", 4, 8), ("Cheese", 5, 9)]

print("Total = ", sum_value())
print(("List = ", food_list()))
update_food_price()
print(lst)