m = float(input("Enter the number of minutes:"))

days= m // (24*60)
m = m % (24*60)

hour = m//(1*60)
m = m %60

seconds = m//(60)
m = m%60

print ("d:",int(days),"h:",int(hour),"m",int(m),"s:",int(seconds))

