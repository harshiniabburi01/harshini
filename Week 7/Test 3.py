#Input from the user
miles = float(input("Enter the number of miles from Bangor to Belfast = "))

fare = 0

#Fare calculations
if miles == 0:
    fare = 2
elif miles <= 5:
    fare = 2 + (4*miles)
elif miles <= 10:
    fare = 2 + (4 * 5) + (3 * (miles - 5))
elif miles > 10:
    fare = 2 + (4 * 5) + (3 * 5) + (2 * (miles - 10))

#Output
print("The total fare from Bangor to Belfast for tom will be = ", fare)
