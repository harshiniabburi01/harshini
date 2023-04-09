#Input
a = float(input("Enter the value of a="))
b = float(input("Enter the value of b="))

#X Calculations

if a == 0:
    if b==0:
        print("It can be any number")

if a==0:
    if b!=0:
        print("There is no real value for x")

if a !=0:
    x = b / a
    print("The value of x =",x)
