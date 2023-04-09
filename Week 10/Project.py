
# MAIN MENU OF THE PROGRAM
# some initial tasks such as loading data from files go here
#load_from_file()
# other information
message = """
********  The Flower Shop program written by Tom ********
Feature 1: Show a customer
Feature 2: Add a flower
...
0: Exit program 
"""
# repeatedly run the main menu
while (True):
    # for testing purpose only
    #show_info()
    # print out all possible choices to users
    print(message)
    # ask the user to select a choice
    x = int(input("Please enter your choice as indicated above: "))
    # get the choice and choose appropriate action
    if x == 1:
        # instead of writing feature 1 - show customer here
        # we write a function and call it here for clarity
        feature_1_show_customer()
    elif x == 2:
        # instead of writing feature 2 - add flower here
        # we write a function and call it here for clarity
        feature_2_add_flower()
    else:
        print("Existing program...")
        break # to stop the while loop
# some finalize tasks such as storing data into files go here
#save_to_file()
# inform the users that the program ended completely
print("Program ended...")