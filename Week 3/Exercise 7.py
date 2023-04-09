#Input a,b,c

a = float(input("Enter the value of a ="))
b = float(input("Enter the value of b="))
c = float(input("Enter the value of c ="))

#Good Set calculations

if a + b == c:
    print("This is a good set")
elif b + c == a:
    print("This is a good set")
elif c == b + a:
    print ("This is a good set")
else:
    print("This is not a good set")