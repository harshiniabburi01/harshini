#Input

Tommiles = float(input("Enter the number of miles from tom's house ="))
Jerrymiles = float(input("Enter the number of miles from jerry's house="))

Tomspeed = float(input("Enter Tom's Speed="))
Jerryspeed = float(input("Enter Jerry's Speed="))

#Time Calcultions

Tomtime = Tommiles/ Tomspeed
Jerrytime = Jerrymiles/Jerryspeed

if Tomtime < Jerrytime:
    print("Tom arrives first")
if Tomtime > Jerrytime:
    print("Jerry arrives first")
else:
    print("The both arrive at the same time")
