import math as m

dia = float(input("Enter the sphere diameter : "))

rad = dia/2
vol = (4/3)*m.pi*(rad**3)
sur = 4*m.pi*(rad**2)

print("The length of the sphere radius is %.4f"%rad)
print("The sphere volume and the surface area are %.4f and %.4f "%(vol,sur))
