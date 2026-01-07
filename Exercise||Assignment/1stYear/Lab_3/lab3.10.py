import math as m

a_paint = float(input("Input the covered area for one paint bottle (cm square): "))
num = float(input("Input the number of the spheres: "))
rad = float(input("Input the number of the spheres: "))

sur_sp = 4*(m.pi)*(rad**2)
t_sphere = sur_sp*num
total = t_sphere/a_paint
total_2 = m.ceil(total)

print("The paint bottlesare needed to paint he surface of spheres is %d."%total_2)
