import bank_client as BC

class user ():
    def __int__(self, username, first_name, last_name, mobile_number):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number

    def show_user_detials (self):
        print ("User Detials")
        print ("Username :", self.username)
        print("Name :", self.first_name, self.last_name)
        print ("Mobile Number:", self.mobile_number)


class bankaccount:
    def __int__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0

    def deposit (self,amount):
        self.amount = amount
        self.balance = self.balance + self,amount
        print ("The Updated Account Balance after deposit : $ ", self.balance)

    def withdraw (self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("There are insufficent funds, transaction caanot be made"
                  "Avaliable Balance = $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print ("The updated account balance after withdrawing funds = $", self.balance)

    def see_balance (self):
        self.show_detials()
        print("The account balance is = $", self.balance)

# class main():

def collect_info():
    username = input("Enter username: ")
    password = input("Enter password: ")
    pwd_conf = input("Confirm password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    try:
        mobile_number = int(input("Enter mobile number: "))
        arr = [username, password, pwd_conf, first_name, last_name, mobile_number]
        return arr
    except:
        return [username, password, pwd_conf, first_name, last_name, 0]


def menu():
    client = BC.bank_client("", "", "", "", "")
    message = """"
    - BelfastDevs Online Banking System -
    [1] Register bank user
    [2] Read bank user details
    [3] Delete bank user 
    [4] Open bank account
    [5] Read bank account details
    [6] Delete bank account
    [7] Perform a transaction
    [8] Read transaction details
    [9] Delete transaction

    0 - Exit program
    """
    while (True):
        print(message)

        askuser = int(input("Please enter an option... :"))
        if askuser == 1:
            info = collect_info()
            client.register(*info)
        elif askuser == 2:
            client.register_password()
        else:
            print("Program closing... Goodbye.")
            break


# def main():
#     menu()
# if __name__ == "__main__":
#     main()
