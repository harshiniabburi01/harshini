#Input
N = int(input("Enter the value of N ="))

#Range of odd numbers
for i in range(1,N+1,1):
    while i == N:
        i = i - 1
        print(i)