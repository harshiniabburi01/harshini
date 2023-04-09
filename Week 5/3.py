N = int(input("Enter a number="))

for i in range (N+1):
    for j in range (i+1):
        print ("+", end = " ")

    for k in range (N-i):
        print ("*", end = " ")
    print()
