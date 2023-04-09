#Input from the user
w = float(input("Enter the lenght of any one side of the backyard = "))
r = float(input("Enter the radius of circular pool = "))
p = float(input("Enter the price of each square meter for artifical grass = "))

#Area calculations
area_backyard = w * w
area_pool =  3.14 * r * r

#Area of grass calcualtion
area_grass = area_backyard - area_pool
#Cost of grass calculation
cost_of_grass = area_grass * p
overall_cost = cost_of_grass + (cost_of_grass * 0.1)

#Output
print("The overall price of artificial grass installation is = ", overall_cost)
