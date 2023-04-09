def check_good_ring(r):
    a = 3.14 * r * r
    if a > 99:
        print("good ring")
    else:
        print("Bad ring")
    return a

r1 = float(input("Enter the radius of ring 1 ="))
check_good_ring(r1)
r2 = float(input("Enter the radius of ring 2 ="))
check_good_ring(r2)
r3 = float(input("Enter the radius of ring 3 ="))
check_good_ring(r3)


