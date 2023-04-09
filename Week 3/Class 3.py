#Input
BMI = float(input("Enter your BMI"))

if BMI < 19:
    y = "Underweight"
elif 19 <= BMI < 25:
    y = "Normal"
elif 25 <= BMI < 30:
    y = "Overweight"
else:
    y = "Obese"

#Output

print("Health Status:",y)
