import math as m

d = float(input("Enter the distance to the building: "))
a = float(input("Enter the elevation angle in degree: "))
a=m.radians(a)
h = d*(m.tan(a))

print("The building height is %.4f"% h)
