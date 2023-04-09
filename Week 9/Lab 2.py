
def total_value():
    sum = 0
    for item in d.values():
        price = item[0]
        quantity = item[1]
        if quantity >= 5:
            value = price * quantity
            sum += value
    return sum


def food_list():
    sub = []

    for k, v in d.items():
        price = v[1]
        if price >= 5:
            sub.append(k)
    return sub

def update_price():
    name = input("Please input name = ")
    quantity = float(input("Please input quantity = "))

    if name not in d:
        print("the food not include in the list")
    else:
        item = d[name]
        item[0] = item[1] + quantity

d = {"Apple": [5, 10], "Banana": [2, 4], "Grape": [4, 8], "Cheese": [5, 9]}


print("Total = ", total_value())
print("List = ", food_list())
update_price()
print(d)

