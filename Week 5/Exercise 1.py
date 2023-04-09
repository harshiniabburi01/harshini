N = int(input("Enter a number="))

for i in range (N):
    for j in range (i + 1):
        print ("+", end = "")

    print ()

for i in range (N):
    for j in range (N- i):
        print ("+", end = "")

    print ()
