def check_good_ring(r):
    a = 3.14 * r *r
    if a > 99:
        return True
    else:
        return False


n = int(input("Enter the value of n = "))

count = 0

for i in range (n):
    r = float(input("Enter r ="))
    g = check_good_ring(r)
    if g == True:
        count = count + 1

print("Number of good rings =", count)