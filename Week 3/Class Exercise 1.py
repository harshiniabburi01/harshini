#Input
name = input("Enter your name:")
height = float(input("Enter your height:"))
weight = float(input("Enter your weight"))

#BMI Calculation
BMI = weight / (height**2)

#Output
if BMI > 25:
    print("You are overweight")

else:
    print(name,"You are not overweight")