#Function to check prime number
def check_prime_number (p):

    for i in range(2, p - 1, 1):
        if p % i == 0:
            return False
        else:
            return True
    return p

#Input
n = int(input("Enter the number of numbers ="))

sum = 0
average = 0
count = 0

#Calcultion and checking for prime avergae
for i in range (n):
    p = int(input("Enter the value of a number = "))
    if p > 1:
        g = check_prime_number(p)
        if g == True:
            count = count + 1
            sum = sum + p
            average = sum / count
        if g == False:
            print("There are no prime numbers")
    else:
        print("There are no positive numbers")

#Output
print("The avg. value of prime numbers among them = ", average)