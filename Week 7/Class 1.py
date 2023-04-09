def weight(x):
    a = x * x
    w = a * 2
    return w

x1 = float(input("Enter the value of a1="))
x2 = float(input("Enter the value of a2="))

sum = weight(x1) + weight(x2)

print("Sum=", sum)