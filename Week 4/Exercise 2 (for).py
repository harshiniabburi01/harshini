#Input
N = int(input("Enter the value of N ="))

#Odd and even lines solution

for i in range (1,N+1,1):
    if i % 2 == 0:
        print("+++++")
    elif i % 2 == 1:
        print("*****")

