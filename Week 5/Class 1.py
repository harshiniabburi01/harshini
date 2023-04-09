#Input
n = int(input("Enter the value of N ="))
m = int(input("Enter the value of M="))

#Calculations and output

for i in range (1,n+1,1):
    if i % 2 == 1:
        for j in range (1,m+1,1):
            print("+", end = " ")
    else:
        for j in range (1, m+1,1):
            print("*", end = " ")
    print()