
def feature_1_show_customer():
    """
    This feature will Show all information of a customer
    """
    customerid = int(input("Enter a valid customer id: "))
    # find the position of the ID in the list of customer
    position = get_customer(customerid)
    # if the id of the customer does not exist
    if position == -1:
        print("We do not have a customer with the matching id ", customerid)
    # if the customer does exists in the system
    else:
        item = lst_customers[position]
        print("Name : ", item[1], " Type : ", item[2], " Price : ", item[3], "Quantity : ", item[4])

def feature_2_add_flower():
    """
    The purpose of this fucntion is to add a flower to the list
    """
    id = int(input("Enter ID : "))
    name = input("Enter name of the flower : ")
    type = input("Enter the type of flower : ")
    price = int(input("Enter the price of the flower : "))
    quantity = int(input("Enter the quantity of the flower :"))
    position = get_flower(id)
    # if the flower id is new in the system
    if position == -1:
        lst_flowers.append([id, name, type, price,quantity])
    # if the flower is existing in the system
    else:
        lst_customers[position] = [id, name, type,price,quantity]
