#Input
N = int(input("Enter the value of N="))

#Odd and even line solution
i = 1

while N >= i:
     if i % 2 == 0:
          print("+++++")
     elif i % 2 == 1:
          print("*****")
     i = i + 1

