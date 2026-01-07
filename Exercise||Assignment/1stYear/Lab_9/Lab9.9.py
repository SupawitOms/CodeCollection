import math as m

def myCylinder():
    v = m.pi*(r*r)*h
    a = (2*m.pi*h*r)+(2*m.pi*(r*r))

    print("The volumn is %.2f and the surface area is %.2f"%(v,a))

r = float(input("Enter the radius r of the cylinder: "))
h = float(input("Enter the height h of the cylinder: "))
myCylinder()