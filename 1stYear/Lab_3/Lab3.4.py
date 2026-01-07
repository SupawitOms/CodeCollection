import numpy as np
import matplotlib.pyplot as plt
import math as m

p1_x = float(input("Enter coordinate X for P1 : "))
p1_y = float(input("Enter coordinate Y for P1 : "))
p2_x = float(input("Enter coordinate X for P2 : "))
p2_y = float(input("Enter coordinate Y for P2 : "))

dia = m.sqrt(((p1_x - p2_x)**2) + ((p1_y - p2_y)**2))
cir = m.pi*dia
rad = cir/(2*m.pi)
area = m.pi*(rad**2)

print("The length of the  circle diameter is %.4f"% dia)
print("The circle area and circumference are %.4f and %.4f"% (area,cir))
