N = int(input("Enter a number ="))

prime_no = True


for i in range(2,N-1,1):
    if N % i == 0:
        prime_no = False


if prime_no == True:
        print("The number is a prime number")
else:
    print("The number is not a prime number")
