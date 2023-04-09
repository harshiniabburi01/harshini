#Input from the user
x = float(input("Enter the speed at which Tom is walking to school  = "))
y = float(input("Enter the speed at which jerry is walking to school = "))

#Total Time Calculations
Tomtime = 1500/x + 15
Jerrytime = 1000/y

#Output
if Tomtime < Jerrytime:
    print("Tom arrives first")
if Tomtime > Jerrytime:
    print("Jerry arrives first")
if Tomtime == Jerrytime:
    print("They both arrive at the same time")

