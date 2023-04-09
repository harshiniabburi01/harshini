x = float(input("Enter the distance of school from Tom's House:"))
y = float(input("Enter the speed at which Tom walks to school:"))

t = (x/y) * 60 + 15
h = t//60

min = t - h * 60


print ("Tom will reach school at:",int(h+8),":",int(min))
