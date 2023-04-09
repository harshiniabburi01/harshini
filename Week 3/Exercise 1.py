#Input

a = float(input("Enter the value of a="))
b = float(input("Enter the value of b="))
c = float(input("Enter the value of c="))

#Max calculation

max = a

if max < b:
    max = b
if max < c:
    max = c

#Output
print("Max value",max)
