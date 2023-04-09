A = int(input("Enter the number of rows ="))
B = int(input("Enter the number of columns ="))

i = 1
j = 1

while i >= A:
    while j >= B:
        j = 1
        print("*", end=" ")
    print()
j = j + 1
i = i + 1